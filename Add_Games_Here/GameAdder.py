import tkinter as tk
import requests

def scrape_games(name):
    exist = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    base_url = "https://www.metacritic.com/game/playstation-4/"

    
    name = name.strip()
    url = base_url + name
    session = requests.Session()
    response = session.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("doesnt exist")
        exist = False
    else:
        print("exists")
        exist = True
    return exist



def add_line():
    line = new_line_entry.get()
    if line:
        with open("meta_names.mtac", "r") as file:
            contents = file.readlines()
            if contents:
                last_line = contents[-1].strip()
                if last_line:
                    line = line + "\n"
        with open("meta_names.mtac", "a") as file:
            if (scrape_games(line)):  
                file.write(line)
    new_line_entry.delete(0, tk.END)
    display_file()






def remove_line():
    with open("meta_names.mtac", "r") as file:
        lines = file.readlines()
    with open("meta_names.mtac", "w") as file:
        for line in lines[:-1]:
            file.write(line)
    new_line_entry.delete(0, tk.END)
    display_file()





def display_file():
    text.config(state="normal")
    with open("meta_names.mtac", "r") as file:
        contents = file.read()
    text.delete("1.0", tk.END)
    text.insert("1.0", contents)
    text.config(state="disabled")
    text.update_idletasks()


root = tk.Tk()

text = tk.Text(root)
text.pack()
display_file()



new_line_entry = tk.Entry(root)
new_line_entry.pack()

add_line_button = tk.Button(root, text="Add Line", command=add_line)
add_line_button.pack()

save_button = tk.Button(root, text="Remove Line", command=remove_line)
save_button.pack()



root.mainloop()
