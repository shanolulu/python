import db_controller
from domain import Entity
import view


ct = db_controller.PRController()
# controller.file_read() 
# read 할 필요가 사라짐(DB사용)

while True:
    view.menu()
    menu = view.input_menu()

    if menu == 1:
        code = view.input_code()
        name, price, color = view.input_entity()
        ct.control_register(Entity(name, price, code, color))
    elif menu == 2:
        ct.control_get_all_entity()
    elif menu == 3:
        code = view.input_code()
        ct.control_get_entity(code)
    elif menu == 4:
        code == view.input_code()
        name, price, color = view.input_entity()
        ct.control_update_entity(Entity(name, price, code, color))
    elif menu == 5:
        code = view.input_code()
        ct.control_delete_entity(code)
    elif menu == 0:
        ct.close()
        break
    else:
        view.message('메뉴는 1,2,3,4,5 중 하나를 골라주세요. (0은 종료)')
        continue