import streamlit as st
from flip_status_class import UpdateOrder_COD_PAID, UpdateOrder_NET_TERMS_PAID, all_admin_orders_accounting_page, payment_method, UpdateOrder_REMITTED, connect_website, UpdateOrder_PARTIAL_PAID, amount_collected, UpdateOrder_SELF_COLLECTED,update_Brand_fee_90_days
import pandas as pd


# Streamit App title
st.set_page_config('Flip Payment Status',page_icon=':arrows_clockwise:',layout='wide')
st.title('Flip Payment Status App')
st.markdown('---')
col1,col2 = st.columns(2)
with col1:
    bearer_token = str(st.text_input("Insert Bearer Token"))
    file = st.file_uploader('Upload list of invoices')
    if file is not None:
        df = pd.read_excel(file,engine='openpyxl')
        df['Invoice'] = df['Invoice'].astype('str') 
        count_invoices = df.shape
        df[['GMV_Collected','TAX_Collected']].fillna(0,inplace=True)
        df[['GMV_Collected','TAX_Collected']] = df[['GMV_Collected','TAX_Collected']].astype('float')
        st.write(f'{count_invoices[0]} Invoices to Flip')
       
    pmt_status = st.radio('Select Payment Status',options=['Paid','Remitted','Partial Paid','Self Collected','90 Days Fees Collected'],index=1)
    if pmt_status == 'Paid':
        paymt_method = st.radio('Choose Payment Method',options=['CASH','CHECK','EFT'])
    elif pmt_status == 'Partial Paid':
        paymt_method = st.radio('Choose Payment Method',options=['CASH','CHECK','EFT'])


def flip_to_paid(headers,list_orders,pmt_method):
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
            "payment_terms" : order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['daysTillPaymentDue']
        }

        payment_method(headers,qb_invoice_data,pmt_method)
        if qb_invoice_data['payment_terms'] == 0 :
            UpdateOrder_COD_PAID(headers,qb_invoice_data)
        else:    
            UpdateOrder_NET_TERMS_PAID(headers,qb_invoice_data)

        st.write(f'{order}{", Pmt terms = "} {qb_invoice_data["payment_terms"]} {" Pmt Method -- "} {pmt_method}')
  

def flip_to_remitted(headers,list_orders):
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
        }

        UpdateOrder_REMITTED(headers,qb_invoice_data)
        st.write(f'{order}{"  "}{" Order Processed "} ')

def flip_to_self_collected(headers,list_orders):
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
        }

        UpdateOrder_SELF_COLLECTED(headers,qb_invoice_data)
        st.write(f'{order}{"  "}{" Order Processed "} ')        


def flip_to_PARTIAL_PAID(headers,list_orders,GMV_Collected,TAX_Collected,pmt_method):

    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
            "gmvCollected" : order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['gmvCollected'],
            "exciseTaxCollected" : order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['exciseTaxCollected'],
        }

        gmv_collected = float(qb_invoice_data['gmv_collected'] + GMV_Collected[order])
        tax_collected = float(qb_invoice_data['exciseTaxCollected'] + TAX_Collected[order])

        amount_collected(headers,qb_invoice_data,gmv_collected,tax_collected)
        UpdateOrder_PARTIAL_PAID(headers,qb_invoice_data)
        payment_method(headers,qb_invoice_data,pmt_method)
        st.write(f'{order}{"  "}{" Order Processed "} ')

def flip_90Days_fees_to_collected(headers,list_orders):
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['brandFeesCollection']['id'],
        }

        update_Brand_fee_90_days(headers,qb_invoice_data)
        st.write(f'{order}{"  "}{" Order Processed "} ')
        
          



st.markdown('---')
left_col,center_col,right_col = st.columns(3)

with center_col:
    st.title('**Powered by HQ**')
    st.image('https://www.dropbox.com/s/twrl9exjs8piv7t/Headquarters%20transparent%20light%20logo.png?dl=1')

with col2:
    if pmt_status == 'Paid':
        try:
            st.title(f'You have selected {pmt_status} Status, and payment method {paymt_method}')
            st.warning('Be sure all the information is correct before submitting.')
            submit_to_paid = st.button('Submit to Paid')
            if submit_to_paid:
                headers = connect_website(bearer_token)
                flip_to_paid(headers,df['Invoice'],paymt_method)
        except NameError:
            st.write('Error, reach out to admin')

    elif pmt_status == 'Partial Paid':
        try:
            st.title(f'You have selected {pmt_status} Status, and payment method {paymt_method}')
            st.warning('Be sure all the information is correct before submitting.')
            submit_to_Partial_paid = st.button('Submit to Partial Paid')
            if submit_to_Partial_paid:
                GMV_collected_dict = dict(zip(df['Invoice'],df['GMV_Collected']))
                TAX_collected_dict = dict(zip(df['Invoice'],df['TAX_Collected']))
                headers = connect_website(bearer_token)
                flip_to_PARTIAL_PAID(headers,df['Invoice'],GMV_collected_dict,TAX_collected_dict,paymt_method)
        except NameError:
            st.write('Error, reach out to admin')

    elif pmt_status == 'Self Collected':
        try:
            st.title(f'You have selected {pmt_status} Status.')
            st.warning('Be sure all the information is correct before submitting.')
            submit_to_self_collected = st.button('Submit to Self Collected')
            if submit_to_self_collected:
                headers = connect_website(bearer_token)
                flip_to_self_collected(headers,df['Invoice'])
        except NameError:
            st.write('Error, reach out to admin')        

    elif pmt_status == '90 Days Fees Collected':
        try:
            st.title(f'You have selected {pmt_status} Status.')
            st.warning('Be sure all the information is correct before submitting.')
            submit_90days_fees_to_collected = st.button('Submit 90Days Fees to Collected')
            if submit_90days_fees_to_collected:
                headers = connect_website(bearer_token)
                flip_90Days_fees_to_collected(headers,df['Invoice'])
        except NameError:
            st.write('Error, reach out to admin')


    else:
        try:
            st.title(f'You have selected {pmt_status} Status.')
            st.warning('Be sure all the information is correct before submitting.')
            submit = st.button('Submit to Remitted')
            if submit:
                headers = connect_website(bearer_token)
                flip_to_remitted(headers,df['Invoice'])
        except NameError:
            st.write('Error, reach out to admin')
            


