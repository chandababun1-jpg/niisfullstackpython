def insert_data():
    r = rollno_entry.get()
    n = name_entry.get()
    m = marks_entry.get()

    if r == "" or n == "" or m == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        con = get_connection()
        cur = con.cursor()

        sql = "INSERT INTO student(rollno,name,marks) VALUES(%s,%s,%s)"
        cur.execute(sql, (r, n, m))

        con.commit()
        con.close()

        messagebox.showinfo("Success", "Record Inserted")

    except Exception as e:
        messagebox.showerror("Error", str(e))