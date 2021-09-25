# import requests
# import openpyxl
#
# params = {
#     'username': 'byhy',
#     'password': '88888888'
# }
# s = requests.Session()
#
# s.post('http://127.0.0.1:8047/api/mgr/signin', data=params)
#
# # customers = [
# #     {
# #         "name": "武汉市桥西医院",
# #         "phonenumber": "13345679934",
# #         "address": "武汉市桥西医院北路"
# #     },
# #     {
# #         "name": "四川大学华西医院",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷37号"
# #     },
# #     {
# #         "name": "四川大学华西医院1",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷38号"
# #     },
# #     {
# #         "name": "四川大学华西医院1",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷39号"
# #     },
# #     {
# #         "name": "武汉市桥西医院1",
# #         "phonenumber": "13345679934",
# #         "address": "武汉市桥西医院北路"
# #     },
# #     {
# #         "name": "四川大学华西医院",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷40号"
# #     },
# #     {
# #         "name": "四川大学华西医院1",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷41号"
# #     },
# #     {
# #         "name": "四川大学华西医院1",
# #         "phonenumber": "028-85422114",
# #         "address": "四川省成都市武侯区国学巷42号"
# #     }
# # ]
# # medicines = [
# #     {
# #         "name": '青霉素盒装3',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装4',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装5',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装6',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装7',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装8',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装9',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装10',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装11',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装12',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     },
# #     {
# #         "name": '青霉素盒装13',
# #         "desc": "青霉素注射液，每支15ml，40支装",
# #         "sn": "YP-32342343"
# #     }
# # ]
# #
# # orders = [
# #     {
# #         "name": "四川华西医院订单001",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单002",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单003",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单004",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单005",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单006",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单007",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单008",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单009",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单010",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }, {
# #         "name": "四川华西医院订单011",
# #         "customerid": 3,
# #         "medicinelist": [
# #             {"id": 16, "amount": 5, "name": "环丙沙星"},
# #             {"id": 15, "amount": 5, "name": "克林霉素"},
# #         ]
# #     }
# # ]
# #
# #
# # def add_costomers(customers):
# #     for costomer in customers:
# #         s.post("http://127.0.0.1:8047/api/mgr/customers",
# #                json={
# #                    "action": "add_customer",
# #                    "data": costomer
# #                })
# #
# #
# # def add_medicines(medicines):
# #     for medicine in medicines:
# #         s.post("http://127.0.0.1:8047/api/mgr/medicines",
# #                json={
# #                    "action": "add_medicine",
# #                    "data": medicine
# #                })
# #
# #
# # def add_orders(orders):
# #     for order in orders:
# #         s.post("http://127.0.0.1:8047/api/mgr/orders",
# #                json={
# #                    "action": "add_order",
# #                    "data": order
# #                })
#
# # add_costomers(customers)
# # add_medicines(medicines)
# # add_orders(orders)
#
# orders =s.get('http://127.0.0.1:8047/api/mgr/customers',
#            params={
#                "action":"list_customer",
#                "pagesize":100,
#                "pagenum":1,
#            }).json()
# print(orders["retlist"])
# title =
