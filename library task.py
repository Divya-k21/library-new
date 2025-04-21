book=[]
def addbook(bookname,autname,bookid):
      booklist = {"name": bookname, "author": autname, "id": bookid}
      book.append(booklist)
      print("added booklist",booklist)
      print("curent books",book)
     
bookname=input("enter a bookname\n")
autname=input("enter a author name\n")
bookid=input("enter a bookid")
addbook(bookname,autname,bookid)
def search_book(user_bookname,user_aut_name,book_id):
      addbook()
      found=false
      for book in book:
            print(book)
            if(addbook['bookname']==user_bookname and
               addbook['autname']==user_aut_name and
               addbook['bookid']==book_id):
                  print("searched data",book)
                  found=True
                  break
            else:
                  print("no data dound")
                  search_book(user_bookname,user_aut_name,book_id)
                  while True:
                       num=input("1.add book 2.search book 3.exit\n")
                       if num=='1':
                            bookname=input("enter a book name ")
                            autname=input("enter a author name ")
                            bookid=int(input("enter a book id "))    
                            addbook( user_bookname, user_aut_name,book_id)
                            print("current book",book)
                            elif num=='2':
                            user_bookname=input("enter a book name ")
                            user_aut_name=input("enter a author name")
                            book_id=int(input("enter a book id "))
                            search_book(user_bookname, user_aut_name,book_id)
                            print("current book",book)
                            elif num=='3':
                            exit
                            else:
                            print("invalid")   