import streamlit as st
from flip_status_class import UpdateOrder_COD_PAID, UpdateOrder_NET_TERMS_PAID, all_admin_orders_accounting_page, payment_method, UpdateOrder_REMITTED, connect_website
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
        list_invoices = df['Invoice'].astype('str').to_list() 
        st.write(f'{int(len(list_invoices))} Invoices to Flip')
       
    pmt_status = st.radio('Select Payment Status',options=['Paid','Remitted'],index=1)
    if pmt_status == 'Paid':
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
        st.write(f'{order}{", Pmt termns = "} {qb_invoice_data["payment_terms"]} {" Pmt Method -- "} {pmt_method}')
        if qb_invoice_data['payment_terms'] == 0 :
            UpdateOrder_COD_PAID(headers,qb_invoice_data)
        else:    
            UpdateOrder_NET_TERMS_PAID(headers,qb_invoice_data)
  

def flip_to_remitted(headers,list_orders):
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(headers,order_number)
        
        qb_invoice_data = {
            "id": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
        }

        st.write(f'{order}{"  "}{" Order Processed "} ')
        UpdateOrder_REMITTED(headers,qb_invoice_data)

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
                flip_to_paid(headers,list_invoices,paymt_method)
        except NameError:
            st.write('Error, reach out to admin')
    else:
        try:
            st.title(f'You have selected {pmt_status} Status.')
            st.warning('Be sure all the information is correct before submitting.')
            submit = st.button('Submit to Remitted')
            if submit:
                headers = connect_website(bearer_token)
                flip_to_remitted(headers,list_invoices)
        except NameError:
            st.write('Error, reach out to admin')


