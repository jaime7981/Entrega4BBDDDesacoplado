import usefullfunc as psfunc
from tabulate import tabulate
from random import randint

### MENU PARA LOCAL
def AgregarLocal():
    print("Agregar local")
    nombre_local = "'" + input("Nombre local: ") + "'"
    calle_local = "'" + input("Direccion local: ") + "'"
    numero_local = input("Numero local: ")
    comuna_local = "'" + input("Comuna local: ") + "'"
    region_local = "'" + input("Region local: ") + "'"
    aceptar_opcion = input("Esta seguro de esta informacion? (S/N) ")
    if aceptar_opcion == "S":
        psfunc.InsertQuerry("locales", ("nombre", "calle", "numero", "comuna", "region"),
                                (nombre_local,
                                    calle_local,
                                    str(numero_local),
                                    comuna_local,
                                    region_local))

def EditarLocal(id_local_seleccionado):
    print("Que Parametro Desea Modificar")
    opcion_editar_local = ["Nombre",
                            "Calle",
                            "Numero",
                            "Comuna",
                            "Region",
                            "Volver Atras"]
    psfunc.DisplayMenu(opcion_editar_local)
    opcion = psfunc.InputOpciones(opcion_editar_local)
    if opcion == 1:
        editar_local = input("Ingresar Nuevo Nombre Local: ")
        psfunc.UpdateQuerry("locales", 
                            "nombre = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado))
    
    elif opcion == 2:
        editar_local = input("Ingresar Nueva Calle Local: ")
        psfunc.UpdateQuerry("locales", 
                            "calle = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado))

    elif opcion == 3:
        editar_local = input("Ingresar Nuevo Numero Local: ")
        psfunc.UpdateQuerry("locales", 
                            "numero = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado))

    elif opcion == 4:
        editar_local = input("Ingresar Nueva Comuna Local: ")
        psfunc.UpdateQuerry("locales", 
                            "comuna = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado))

    elif opcion == 5:
        editar_local = input("Ingresar Nueva Region Local: ")
        psfunc.UpdateQuerry("locales", 
                            "region = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado))
    
    elif opcion == 6:
        pass

def AgregarMenu(id_local_seleccionado):
    print("Agregar Menu")
    nombre_menu = "'" + input("Nombre Menu: ") + "'"
    precio_menu = input("Precio Menu: ")
    psfunc.InsertQuerry("menues", 
                        ("nombre", "precio", "id_local"),
                        (nombre_menu, str(precio_menu), str(id_local_seleccionado)))

def EditarMenu(id_local_seleccionado, id_menu_seleccionado):
    print("Que Parametro Desea Modificar")
    opcion_editar_menu = ["Nombre",
                          "Precio",
                          "Volver Atras"]
    psfunc.DisplayMenu(opcion_editar_menu)
    opcion = psfunc.InputOpciones(opcion_editar_menu)
    if opcion == 1:
        editar_local = input("Ingresar Nuevo Nombre Menu: ")
        psfunc.UpdateQuerry("locales", 
                            "nombre = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado) \
                            + " id_menu = " + str(id_menu_seleccionado))
    
    elif opcion == 2:
        editar_local = input("Ingresar Nuevo Precio Menu: ")
        psfunc.UpdateQuerry("locales", 
                            "calle = '" + str(editar_local) + "'",
                            "id_local = " + str(id_local_seleccionado)\
                            + " id_menu = " + str(id_menu_seleccionado))
    
    elif opcion == 3:
        pass

def EliminarMenu(id_local_seleccionado ,id_menu_seleccionado):
    delete_product_from_menu = input("Seguro que desea eliminar este menu? (S/N) ")
    if delete_product_from_menu == "S":
        psfunc.DeleteQuerry("menues"
                            ,"id_menu = " + str(id_menu_seleccionado) + \
                            " AND id_local = " + str(id_local_seleccionado))


def EliminarProductoMenu(id_menu_seleccionado):
    id_producto_seleccionado = psfunc.QuerryOptionIdCheck("SELECT mp.id_producto FROM menu_producto mp INNER JOIN \
                                            (SELECT men.id_menu FROM menues men WHERE id_menu = " + str(id_menu_seleccionado) + ") AS t1 ON mp.id_menu = t1.id_menu",
                                            "Ingresar ID producto: ")
    if id_producto_seleccionado != 0:
        delete_product_from_menu = input("Eliminar el producto del menu? (S/N) ")
        if delete_product_from_menu == "S":
            psfunc.DeleteQuerry("menu_producto"
                                , "id_menu = " + str(id_menu_seleccionado) + \
                                    " AND id_producto = " + str(id_producto_seleccionado))

def VerMenus(id_local_seleccionado, menu_shoping_cart, product_shoping_cart):
    while True:
        psfunc.PrintQuerry("SELECT * FROM menues WHERE id_local = " + str(id_local_seleccionado))
        opcion_menues = ["Seleccionar Menu",
                        "Agregar Menu",
                        "Volver Atras"]
        psfunc.DisplayMenu(opcion_menues)
        opcion = psfunc.InputOpciones(opcion_menues)
        if opcion == 1:
            id_menu_seleccionado = psfunc.QuerryOptionIdCheck("SELECT id_menu FROM menues WHERE id_local = " + str(id_local_seleccionado),
                                                              "Ingresar id menu: ")
            if id_menu_seleccionado != 0:
                while True:
                    psfunc.PrintQuerry("SELECT pr.id_local, pr.id_producto, pr.nombre, pr.precio, pr.id_descuento \
                                    FROM productos pr INNER JOIN \
                                    (SELECT mp.id_producto FROM menu_producto mp INNER JOIN \
                                    (SELECT men.id_menu FROM menues men WHERE id_menu = " + str(id_menu_seleccionado) + \
                                    ") AS t1 ON mp.id_menu = t1.id_menu) AS t2 ON pr.id_producto = t2.id_producto")

                    opcion_menues = ["Agregar Menu Al Carrito",
                                     "Eliminar Producto Del Menu",
                                     "Editar Menu",
                                     "Eliminar Menu",
                                     "Descuento",
                                     "Volver Atras"]
                    psfunc.DisplayMenu(opcion_menues)
                    opcion = psfunc.InputOpciones(opcion_menues)

                    if opcion == 1:
                        psfunc.AddToCart(id_menu_seleccionado, False, menu_shoping_cart, product_shoping_cart)
                        print("Menu Agregado Al Carrito")

                    elif opcion == 2:
                        EliminarProductoMenu(id_menu_seleccionado)
                        
                    elif opcion == 3:
                        EditarMenu(id_local_seleccionado, id_menu_seleccionado)

                    elif opcion == 4:
                        EliminarMenu(id_local_seleccionado, id_menu_seleccionado)

                    elif opcion == 5:
                        desc = psfunc.SelectQuerry("SELECT * FROM menues FULL JOIN (SELECT * FROM descuentos) AS t1 ON t1.id_descuento = menues.id_descuento\
                             WHERE id_menu = " + str(id_menu_seleccionado) + " AND id_local = " + str(id_local_seleccionado))
                        if desc:
                            psfunc.DeleteQuerry("descuentos", "id_descuento = " + str(desc[0][0]))
                        else:
                            print("Crear Descuento")
                            try:
                                valor = int(input("Valor del descuento: "))
                                tipo = input("Descuento Por Valor(N)/Porcentaje(P)")
                                if tipo == "P" or tipo == "N":
                                    psfunc.InsertQuerry("descuentos", (), (tipo, str(valor)))
                                else:
                                    print("Opcion no valida")
                            except:
                                print("Valor no valido")

                    elif opcion == 6:
                        break

        elif opcion == 2:
            AgregarMenu(id_local_seleccionado)

        elif opcion == 3:
            break

### VER PRODUCTOS

def Productos(id_local_seleccionado, menu_shoping_cart, product_shoping_cart):
    while True:
        psfunc.PrintQuerry("SELECT pr.id_producto, pr.nombre, pr.precio, t1.valor FROM productos pr FULL JOIN\
        (SELECT * FROM descuentos) AS t1 ON pr.id_descuento = t1.id_descuento WHERE pr.id_local = " + str(id_local_seleccionado))
        opcion_local_productos = ["Seleccionar Producto",
                                    "Agregar Producto",
                                    "Volver Atras"]
        psfunc.DisplayMenu(opcion_local_productos)
        opcion = psfunc.InputOpciones(opcion_local_productos)
        if opcion == 1:
            id_producto_seleccionado = psfunc.QuerryOptionIdCheck("SELECT id_producto FROM productos WHERE id_local = " + str(id_local_seleccionado), 
                                    "Ingresar id producto: ")
            if id_producto_seleccionado != 0:
                while True:
                    psfunc.PrintQuerry("SELECT * FROM locales WHERE id_local = " + str(id_local_seleccionado))
                    opcion_local_id = ["Agregar Al Carrito",
                                        "Agregar A Menu",
                                        "Editar Producto",
                                        "Eliminar Producto",
                                        "Descuento",
                                        "Volver Atras"]
                    psfunc.DisplayMenu(opcion_local_id)
                    opcion = psfunc.InputOpciones(opcion_local_id)
                    if opcion == 1:
                        psfunc.AddToCart(id_producto_seleccionado, True, menu_shoping_cart, product_shoping_cart)
                    
                    elif opcion == 2:
                        psfunc.PrintQuerry("SELECT * FROM menues WHERE id_local = " + str(id_local_seleccionado))
                        id_menu_seleccionado = psfunc.QuerryOptionIdCheck("SELECT id_menu FROM menues WHERE id_menu = " + str(id_menu_seleccionado),
                                            "Ingresar id menu: ")
                        if id_menu_seleccionado != 0:
                            pr_men = psfunc.SelectQuerry("SELECT * FROM menu_producto WHERE id_menu = " + str(id_menu_seleccionado) + " AND id_producto = " + str(id_producto_seleccionado))
                            if pr_men:
                                ctd_pedido = pr_men[0][2]
                                psfunc.UpdateQuerry("menu_producto", "cantidad_producto = " + str(ctd_pedido + 1), "id_menu = " + str(id_menu_seleccionado) + " AND id_producto = " + str(id_producto_seleccionado))
                            else:
                                psfunc.InsertQuerry("menu_producto", (), (str(id_menu_seleccionado), str(id_producto_seleccionado), str(1)))

                    elif opcion == 3:
                        print("Que Parametro Desea Modificar")
                        opcion_editar_menu = ["Nombre",
                                            "Precio",
                                            "Volver Atras"]
                        psfunc.DisplayMenu(opcion_editar_menu)
                        opcion = psfunc.InputOpciones(opcion_editar_menu)
                        if opcion == 1:
                            editar_producto = input("Ingresar Nuevo Nombre Producto: ")
                            psfunc.UpdateQuerry("productos", 
                                                "nombre = '" + str(editar_producto) + "'",
                                                "id_local = " + str(id_local_seleccionado) \
                                                + " id_producto = " + str(id_producto_seleccionado))
                        
                        elif opcion == 2:
                            editar_producto = input("Ingresar Nuevo Precio Producto: ")
                            psfunc.UpdateQuerry("productos", 
                                                "precio = '" + str(editar_producto) + "'",
                                                "id_local = " + str(id_local_seleccionado)\
                                                + "id_producto = " + str(id_producto_seleccionado))
                        
                        elif opcion == 3:
                            pass
                    
                    elif opcion == 4:
                        delete_product_from_menu = input("Eliminar el producto del local? (S/N) ")
                        if delete_product_from_menu == "S":
                            psfunc.DeleteQuerry("productos"
                                                , "id_producto = " + str(id_producto_seleccionado) + \
                                                " AND id_local = " + str(id_local_seleccionado))

                    elif opcion == 5:
                        desc = psfunc.SelectQuerry("SELECT * FROM productos FULL JOIN (SELECT * FROM descuentos) AS t1 ON t1.id_descuento = productos.id_descuento\
                             WHERE id_producto = " + str(id_producto_seleccionado) + " AND id_local = " + str(id_local_seleccionado))
                        if desc:
                            psfunc.DeleteQuerry("descuentos", "id_descuento = " + str(desc[0][0]))
                        else:
                            print("Crear Descuento")
                            try:
                                valor = int(input("Valor del descuento: "))
                                tipo = input("Descuento Por Valor(N)/Porcentaje(P)")
                                if tipo == "P" or tipo == "N":
                                    psfunc.InsertQuerry("descuentos", (), (tipo, str(valor)))
                                else:
                                    print("Opcion no valida")
                            except:
                                print("Valor no valido")

                    elif opcion == 6:
                        break

        elif opcion == 2:
            print("Agregar Producto")
            nombre_producto = "'" + input("Nombre Producto: ") + "'"
            precio_producto = input("Precio Producto: ")
            psfunc.InsertQuerry("productos", 
                                ("nombre", "precio", "id_local"),
                                (nombre_producto, str(precio_producto), str(id_local_seleccionado)))

        elif opcion == 3:
            break

### RATING
def Rating(id_local_seleccionado, id_user):
    while True:
        psfunc.PrintQuerry("SELECT * FROM usuario_rating WHERE id_local = " + str(id_local_seleccionado) + " AND id_usuario = " + str(id_user))
        opcion_local_productos = ["Agregar Rating",
                                    "Editar Rating",
                                    "Volver Atras"]
        psfunc.DisplayMenu(opcion_local_productos)
        opcion = psfunc.InputOpciones(opcion_local_productos)
        if opcion == 1:
            try:
                rat = int(input("Ingresar Rating (1-5): "))
                if rat > 0 and rat < 6:
                    psfunc.InsertQuerry("usuario_rating", (), (str(id_user), str(id_local_seleccionado), str(rat)))
                else:
                    print("Opcion No Valida")
            except:
                print("Opcion No Valida")

        elif opcion == 2:
            try:
                rat = int(input("Ingresar Nuevo Rating (1-5): "))
                if rat > 0 and rat < 6:
                    psfunc.UpdateQuerry("usuario_rating", "puntuacion = " + str(rat), "id_usuario = " + str(id_user) + " AND id_local = " + str(id_local_seleccionado))
                else:
                    print("Opcion No Valida")
            except:
                print("Opcion No Valida")

        elif opcion == 3:
            break

### MENU PRINCIPAL DE LOCALES
def MenuLocales(login_nombre_usuario, menu_shoping_cart, product_shoping_cart, id_user):
    while True:
        psfunc.PrintQuerry("SELECT * FROM locales")
        opciones_locales = ["Seleccionar Local",
                            "Agregar Local",
                            "Volver Atras"]
        psfunc.DisplayMenu(opciones_locales)
        opcion = psfunc.InputOpciones(opciones_locales)
        if opcion == 1:
            id_local_seleccionado = psfunc.QuerryOptionIdCheck("SELECT id_local FROM locales", 
                                                        "Ingresar id local: ")
            if id_local_seleccionado != 0:
                while True:
                    psfunc.PrintQuerry("SELECT * FROM locales WHERE id_local = " + str(id_local_seleccionado))
                    opcion_local_id = ["Editar Local",
                                        "Eliminar Local",
                                        "Ver Menus",
                                        "Ver Productos",
                                        "Categorias",
                                        "Favorito",
                                        "Rating",
                                        "Volver Atras"]
                    psfunc.DisplayMenu(opcion_local_id)
                    opcion = psfunc.InputOpciones(opcion_local_id)
                    if opcion == 1:
                        EditarLocal(id_local_seleccionado)

                    elif opcion == 2:
                        delete_check = input("Seguro que desea eliminar este local (S/N) ")
                        if delete_check == "S":
                            psfunc.DeleteQuerry("locales", "id_local = " + str(id_local_seleccionado))

                    elif opcion == 3:
                        VerMenus(id_local_seleccionado, menu_shoping_cart, product_shoping_cart)

                    elif opcion == 4:
                        Productos(id_local_seleccionado, menu_shoping_cart, product_shoping_cart)

                    elif opcion == 5:
                        while True:
                            psfunc.PrintQuerry("SELECT DISTINCT ON (cat.id_categoria)  cat.id_categoria, cat.nombre FROM categorias cat INNER JOIN (SELECT lc.id_local, t1.id_categoria FROM locales lc \
                                FULL JOIN (SELECT * FROM categoria_local) AS t1 ON lc.id_local = t1.id_local WHERE lc.id_local = " + str(id_local_seleccionado) + ") AS t2\
                                ON t2.id_categoria = cat.id_categoria ORDER BY cat.id_categoria")
                            opcion_local_id = ["Agregar Categoria",
                                                "Eliminar Categoria",
                                                "Volver Atras"]
                            psfunc.DisplayMenu(opcion_local_id)
                            opcion = psfunc.InputOpciones(opcion_local_id)
                            if opcion == 1:
                                print("Agregar Categoria")
                                psfunc.PrintQuerry("SELECT DISTINCT ON (cat.id_categoria) cat.id_categoria, cat.nombre FROM categorias cat INNER JOIN (SELECT lc.id_local, t1.id_categoria FROM locales lc \
                                FULL JOIN (SELECT * FROM categoria_local) AS t1 ON lc.id_local = t1.id_local WHERE lc.id_local NOT IN (" + str(id_local_seleccionado) + ")) AS t2\
                                ON t2.id_categoria = cat.id_categoria ORDER BY cat.id_categoria")
                                id_categoria_seleccionada = psfunc.QuerryOptionIdCheck("SELECT cat.id_categoria FROM categorias cat INNER JOIN (SELECT lc.id_local, t1.id_categoria FROM locales lc \
                                FULL JOIN (SELECT * FROM categoria_local) AS t1 ON lc.id_local = t1.id_local WHERE lc.id_local NOT IN (" + str(id_local_seleccionado) + ")) AS t2\
                                ON t2.id_categoria = cat.id_categoria", 
                                    "Ingresar id categoria: ")
                                if id_categoria_seleccionada != 0:
                                    psfunc.InsertQuerry("categoria_local", (), (str(id_local_seleccionado), str(id_categoria_seleccionada)))

                            elif opcion == 2:
                                print("Eliminar Categoria")
                                id_categoria_seleccionada = psfunc.QuerryOptionIdCheck("SELECT cat.id_categoria FROM categorias cat INNER JOIN (SELECT lc.id_local, t1.id_categoria FROM locales lc \
                                FULL JOIN (SELECT * FROM categoria_local) AS t1 ON lc.id_local = t1.id_local WHERE lc.id_local = " + str(id_local_seleccionado) + ") AS t2\
                                ON t2.id_categoria = cat.id_categoria", 
                                    "Ingresar id categoria: ")
                                if id_categoria_seleccionada != 0:
                                    psfunc.DeleteQuerry("categoria_local", "id_local = " + str(id_local_seleccionado) + " AND id_categoria = " + str(id_categoria_seleccionada))

                            elif opcion == 3:
                                break

                    elif opcion == 6:
                        fav = psfunc.SelectQuerry("SELECT * FROM usuario_favoritos WHERE id_local = " + str(id_local_seleccionado) + " AND id_usuario = " + str(id_user))
                        if fav:
                            psfunc.DeleteQuerry("usuario_favoritos", "id_local = " + str(id_local_seleccionado) + " AND id_usuario = " + str(id_user))
                            print("Eliminado de favoritos")
                        else:
                            psfunc.InsertQuerry("usuario_favoritos", (), (str(id_user), str(id_local_seleccionado)))
                            print("Agregado a favoritos")

                    elif opcion == 7:
                        Rating(id_local_seleccionado, id_user)

                    elif opcion == 8:
                        break

        elif opcion == 2:
            AgregarLocal()

        elif opcion == 3:
            break


### MENU PARA CARRITO
def ShopingCart(menu_shoping_cart, product_shoping_cart, id_user):
    descuento_carrito = 0
    direccion_pedido = ""
    while True:
        general_cart = []
        for a in menu_shoping_cart:
            menu_on_cart = psfunc.SelectQuerry("SELECT * FROM menues WHERE id_menu = " + str(a))
            general_cart.append(menu_on_cart[0])
        for a in menu_shoping_cart:
            menu_on_cart = psfunc.SelectQuerry("SELECT * FROM productos WHERE id_producto = " + str(a))
            general_cart.append(menu_on_cart[0])
        
        print(tabulate(general_cart, 
                        headers=["ID Item", "ID Local", "Descuento", "Nombre", "Precio"],
                        tablefmt="psql"))
        opciones_carrito = ["Eliminar Item",
                            "Vaciar Carrito",
                            "Eligir Promocion",
                            "Elegir Direccion",
                            "Confirmar Pedido",
                            "Volver Atras"]
        psfunc.DisplayMenu(opciones_carrito)
        opcion = psfunc.InputOpciones(opciones_carrito)
        if opcion == 1:
            try:
                id_item = int(input("Ingresar ID item a eliminar: "))
                id_local = int(input("Ingresar ID del local: "))

                for local in range(len(general_cart)):
                    if id_item == general_cart[local][0]:
                        if id_local == general_cart[local][1]:
                            try:
                                menu_shoping_cart.remove(general_cart[local][0])
                            except:
                                pass
                            try:
                                product_shoping_cart.remove(general_cart[local][0])
                            except:
                                pass
                            print("Item eliminado")
                            
            except:
                print("Valor no valido")

        elif opcion == 2:
            psfunc.ClearShopingCart(menu_shoping_cart, product_shoping_cart)

        elif opcion == 3:
            if psfunc.PrintQuerry("SELECT pr.id_codigo, pr.nombre, pr.fecha_venc, pr.descripcion FROM promociones pr \
                                FULL JOIN (SELECT * FROM promocion_usuario) AS t1 ON t1.id_codigo = pr.id_codigo\
                                WHERE t1.id_usuario = " + str(id_user)):
                opcion_seleccionar_promocion = psfunc.QuerryOptionIdCheck("SELECT pr.id_codigo FROM promociones pr \
                                    FULL JOIN (SELECT * FROM promocion_usuario) AS t1 ON t1.id_codigo = pr.id_codigo\
                                    WHERE t1.id_usuario = " + str(id_user), "Seleccionar Promocion:")
                
                if opcion_seleccionar_promocion != 0:
                    descuento_carrito = psfunc.SelectQuerry("SELECT pr.monto FROM promociones pr \
                                    FULL JOIN (SELECT * FROM promocion_usuario) AS t1 ON t1.id_codigo = pr.id_codigo\
                                    WHERE t1.id_usuario = " + str(id_user) + " AND pr.id_codigo = " + str(opcion_seleccionar_promocion))

                    descuento_carrito = descuento_carrito[0][0]

        elif opcion == 4:
            if psfunc.PrintQuerry("SELECT * FROM direcciones dir FULL JOIN (SELECT * FROM usuario_direccion) AS t1 ON t1.id_direccion = dir.id_direccion WHERE t1.id_usuario = " + str(id_user)):
                opcion_seleccionar_direccion = psfunc.QuerryOptionIdCheck("SELECT dir.id_direccion FROM direcciones dir FULL JOIN (SELECT * FROM usuario_direccion) AS t1 ON t1.id_direccion = dir.id_direccion WHERE t1.id_usuario = " + str(id_user),
                                                                        "Seleccione ID direccion: ")
                if opcion_seleccionar_direccion != 0:
                    direccion_pedido_aux = psfunc.SelectQuerry("SELECT dir.nombre, dir.calle, dir.numero, dir.comuna, dir.region FROM direcciones dir FULL JOIN (SELECT * FROM usuario_direccion) AS t1 ON t1.id_direccion = dir.id_direccion WHERE t1.id_usuario = " + str(id_user) + " AND id_direccion = " + str(opcion_seleccionar_direccion))
                    direccion_pedido = direccion_pedido_aux[0][0], direccion_pedido_aux[0][1], direccion_pedido_aux[0][2], direccion_pedido_aux[0][3], direccion_pedido_aux[0][4]

        elif opcion == 5:
            print("Confirmar Pedido")
            if len(general_cart) >= 0:
                if len(direccion_pedido) > 0:
                    suma_carro = 0
                    for local in range(len(general_cart)):
                        suma_carro += general_cart[local][4]

                    print("Calcular Pedido")
                    print("Direccion: ", direccion_pedido)
                    print("Descuento: ", str(descuento_carrito))
                    print("Total Pedido: ", suma_carro)
                    confirmar_pedido = input("Desea Confirmar Pedido? (S/N)")
                    if confirmar_pedido == "S":
                        repartidores_seleccionar = psfunc.SelectQuerry("SELECT id_repartidor FROM repartidores")
                        random_id = randint(0,len(repartidores_seleccionar))
                        print("Sera atendido por")
                        psfunc.PrintQuerry("SELECT * FROM repartidores WHERE id_repartidor = " + str(random_id))

                else:
                    print("No ha escogido una direccion de envio")
            else:
                print("No hay productos en el carro")

        elif opcion == 6:
            break

