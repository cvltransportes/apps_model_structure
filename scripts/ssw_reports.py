



from priority_classes.ssw.ssw101 import Ssw101
# from priority_classes..ssw101 import Ssw101




def verify_if_exists_ssw_101(items, n_pedido_name_column):
    for index, row in items.iterrows():
        n_pedido = row[n_pedido_name_column]
        print(n_pedido)


    # with Ssw101() as ssw:
    #     # ssw.init_browser()
    #     # ssw.login()
    #     for i, item in enumerate(items):
    #         try:
    #             n_pedido = item[n_pedido_name_column]
    #             print(n_pedido)
    #         except Exception as e:
    #             pass

def test_101():
    with Ssw101() as ssw:
        ssw.init_browser()
        ssw.login()
        response = ssw.op101('info', t_nro_pedido='253755970', act='P6', if_many_ctrc_filter_by={'<f1>': 'PBA899099-9'})
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n-------\n\n\n\n\n\n\n\n\n\n\n\n{response.text}")

    