from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tkinter import *
from tkinter import messagebox

def test():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    search = driver.find_element(By.ID, "searchInput")
    search.send_keys(en_text.get())
    search.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    
    heading = wait.until(expected_conditions.presence_of_element_located((By.ID, "firstHeading")))
    
    if en_text.get().lower() in heading.text.lower():
        messagebox.showinfo("Атотест","Тест прошёл успешно!")
    else:
        messagebox.showinfo("Автотест", "Тест не пройден!")

    driver.quit()

window = Tk()

window.title("Автотест википедии")
window.geometry('400x300')

frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

lb = Label(frame, text = "Автотест википедии")
lb.grid(row=1, column=1, pady=10)

lb_text = Label(frame, text = "Какого слова вы хотите произвести автотест?")
lb_text.grid(row=3, column=1)

en_text = Entry(frame)
en_text.grid(row=4, column=1)

btn = Button(frame, text="Поиск", command=test)
btn.grid(row=5, column=1, pady=5)

window.mainloop()