import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_LOGIN = "https://www.saucedemo.com/"
USER_VALIDO = "standard_user"
PASS_VALIDO = "secret_sauce"

def realizar_login(driver):
    driver.get(URL_LOGIN)
    wait = WebDriverWait(driver, 10)
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    user_input.clear()
    user_input.send_keys(USER_VALIDO)
    pass_input.clear()
    pass_input.send_keys(PASS_VALIDO)
    login_btn.click()

def test_login_success(driver):
    driver.get(URL_LOGIN)
    realizar_login(driver)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url
    page_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert page_title.text == "Products"
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert app_logo.text == "Swag Labs"

def test_inventory_navigation(driver):
    realizar_login(driver)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    assert driver.title == "Swag Labs"
    productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(productos) > 0
    primer_producto = productos[0]
    nombre_prod = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_prod = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\n--- Primer Producto Encontrado ---")
    print(f"Nombre: {nombre_prod}")
    print(f"Precio: {precio_prod}")
    print(f"---------------------------------\n")
    assert nombre_prod != ""
    assert precio_prod.startswith("$")
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_btn.is_displayed()
    filtro_container = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro_container.is_displayed()

def test_add_to_cart_and_verify(driver):
    realizar_login(driver)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
    nombre_esperado = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    btn_add_to_cart = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    assert btn_add_to_cart.text.lower() == "add to cart"
    btn_add_to_cart.click()
    carrito_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert carrito_badge.text == "1"
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    icono_carrito.click()
    wait.until(EC.url_contains("/cart.html"))
    items_carrito = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    assert len(items_carrito) == 1
    nombre_en_carrito = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre_esperado
