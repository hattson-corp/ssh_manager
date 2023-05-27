import os
def install():
    print("installing dependencies .......")
    os.system("sudo apt update ;"
              "suod  apt install python3;"
              " sudo apt install python3-pip;"
              " pip3 install console-menu;"
              "pip3 install flask;"
              " pip3 install crypy;"
              " pip3 install requests ;"
              " pip3 install python-daemon ;"
              " sudo apt install screen ")
install()
from time import sleep
import flask
import daemon

try:
    import requests as rq
except:
    oa.system("apt install python3-pip  ")
    os.system("pip3 install requests")
import subprocess
import time
import crypt

try:
    import consolemenu
    from consolemenu import *
    from consolemenu.items import *
except:
    os.system("apt install python3-pip ; pip3 install console-menu requests ")
    print("[+] All done run the program again !")


class manager:
    def __init__(self):
        self.web = False

    def web(self):
        self.webDelUsers = []
        app = flask.Flask(__name__)

        @app.route("/connections")
        def connections():
            user_info = self.show()
            splited_user = []
            for user in user_info:
                splited_user.append("<tr><th>{}</th><th>{}</th></tr>".format(user[0], user[1]))
                print(splited_user)
            splited_user = "".join(splited_user)
            print(splited_user)
            index_html = """
            <!DOCTYPE html>
                <html>
                    <title>Hattson Server Manager</title>

                    <head>
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                        <style>
                            body{{
                                font-family: 'Alkatra', cursive;
                                font-size: 30px;
                                background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                background-repeat: no-repeat;
                                background-attachment: fixed;
                                background-size: cover;
                                color: white;
                            }}
                            #main{{
                                text-align: center;
                                margin-left: auto;
                                margin-right: auto;
                            }}
                            th{{
                                border: 5px;
                                border-color: #494949;
                                border-style: groove;
                            }}
                        </style>
                    </head>
                    <body>
                        <div id='main'>
                            <h1><p>Hattson Server Manger Connections </p></h1>
                        </div>
                        <div id="main">
                            <table id="main">
                                <tr>
                                    <th>USERNAME</th>
                                    <th>CONNECTIONS</th>
                                </tr>
                            {}
                            </table>
                        </div>
                    <body>
                </html>
            """.format(splited_user)
            return index_html

        @app.route("/")
        def index():
            index_html = '''
                <!DOCTYPE html>
                <html>
                <head>
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">

                    <title>Hattson Server Manager</title>
                    <style>

                        body{{
                            font-family: 'Alkatra', cursive;
                            font-size: 30px;
                            background-color: black;
                            background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            background-size: cover;
                            color: white;
                        }}
                        .button{{
                            font-family: 'Alkatra', cursive;
                            font-family: 'Tillana', cursive;
                            font-size: 30px;
                            color : white;
                            cursor: pointer;
                            outline: none;
                            border: none;
                            border-radius: 15px;
                            box-shadow: 0 9px #999;
                            background-color: transparent;
                            border: gray 2px;


                        }}


                        .button:hover {{background-color: #aaafab}}

                        .button:active {{
                          background-color: #3e8e41;
                          box-shadow: 0 5px #666;
                          transform: translateY(4px);
                        }}
                        #rainbow {{
                            background-image: -webkit-gradient( linear, left top, right top, color-stop(0, #f22), color-stop(0.15, #f2f), color-stop(0.3, #22f), color-stop(0.45, #2ff), color-stop(0.6, #2f2),color-stop(0.75, #2f2), color-stop(0.9, #ff2), color-stop(1, #f22) );
                            background-image: gradient( linear, left top, right top, color-stop(0, #f22), color-stop(0.15, #f2f), color-stop(0.3, #22f), color-stop(0.45, #2ff), color-stop(0.6, #2f2),color-stop(0.75, #2f2), color-stop(0.9, #ff2), color-stop(1, #f22) );
                            color:transparent;
                            -webkit-background-clip: text;
                            background-clip: text;
                        }}
                    </style>
                </head>
                <body>
                    <div style="text-align:center">
                        <h1><p id="rainbow">Peter Hattson Server Manager</p></h1>
                    </div>
                    <div style="text-align:center">
                        <button class="button" onclick="window.location = '/install'">Install</button>
                        <button class="button" onclick="window.location ='/adduser'">Create User</button>
                        <button class="button" onclick="window.location ='/deluser'">Delete User</button>
                        <button class="button" onclick="window.location ='/connections'">Show Connections</button>
                        <button class="button">About</button>
                    </div>


                </body>
                </html>
            '''.format()
            return index_html

        @app.route("/install")
        def install():
            self.install()
            index_html = '''
            <!DOCTYPE html>
                <html>
                    <title>Hattson Server Manager</title>
                    <head>
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                        <style>
                            body{{
                                font-family: 'Alkatra', cursive;
                                font-size: 30px;
                                background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                background-repeat: no-repeat;
                                background-attachment: fixed;
                                background-size: cover;
                                color: white;
                            }}
                            button{{
                                font-family: 'Alkatra', cursive;
                                font-family: 'Tillana', cursive;
                                font-size: 30px;
                                color : white;
                                cursor: pointer;
                                outline: none;
                                border: none;
                                border-radius: 15px;
                                box-shadow: 0 9px #999;
                                background-color: transparent;
                                border: gray 2px;


                            }}


                            button:hover {{background-color: #aaafab}}

                            button:active {{
                              background-color: #3e8e41;
                              box-shadow: 0 5px #666;
                              transform: translateY(4px);
                            }}
                            #main{{
                                text-align: center;
                                margin-left: auto;
                                margin-right: auto;
                            }}

                        </style>
                    </head>
                    <body>
                        <div id='main'>
                            <h1><p>Hattson Server Manger Installing Section</p></h1>
                        </div>
                        <div id="main">
                            <p id='main'> Installation completed !</p>
                            <button class="button" onclick="window.location = '/';"> Back to menu</button>
                        </div>
                    <body>
                </html>
            '''.format()
            return index_html

        @app.route("/adduser")
        def adduser():
            index_html = '''
            <!DOCTYPE html>
                <html>
                    <title>Hattson Server Manager</title>
                    <head>
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                        <style>
                            body{{
                                font-family: 'Alkatra', cursive;
                                font-size: 30px;
                                background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                background-repeat: no-repeat;
                                background-attachment: fixed;
                                background-size: cover;
                                color: white;
                            }}
                            button{{
                                font-family: 'Alkatra', cursive;
                                font-family: 'Tillana', cursive;
                                font-size: 30px;
                                color : white;
                                cursor: pointer;
                                outline: none;
                                border: none;
                                border-radius: 15px;
                                box-shadow: 0 9px #999;
                                background-color: transparent;
                                border: gray 2px;


                            }}


                            button:hover {{background-color: #aaafab}}

                            button:active {{
                              background-color: #3e8e41;
                              box-shadow: 0 5px #666;
                              transform: translateY(4px);
                            }}
                            #main{{
                                text-align: center;
                                margin-left: auto;
                                margin-right: auto;
                            }}
                            #input{{
                                opacity: 0.3;
                                border-radius: 15px;
                                font-family: 'Alkatra', cursive;
                                font-family: 'Tillana', cursive;
                                font-size: 20px;
                                margin-left: auto;
                                margin-right: auto;
                                color: black;
                                width: 150px;
                                height: 30px;   
                                }}
                        </style>
                    </head>
                    <body>
                        <div id='main'>
                            <h1><p>Hattson Server Manger Adding New User</p></h1>
                        </div>
                        <div id="main">
                            <form action='/useradd' method="post">
                                <div id='main'> Username:
                                    <input id='input' name='username' type='text'> 
                                </div>
                                <div id='main'> Password:
                                    <input id='input' name='password' type='text'> 
                                </div>
                                <div id='main'> Time Limit in days:
                                    <input id='input' name='limit' type='text'> 
                                </div>
                                <div id='main'> Number of Clients:
                                    <input id='input' name='client' type='text'> 
                                </div>
                                <div id='main'> Port:
                                    <input id='input' type='number' name='port' value='2280' min='22' max='65535'> 
                                </div>
                                <button class="button" type='submit' > Create User</button>
                            </form>
                        </div>
                    <body>
                </html>
            '''.format()
            return index_html

        @app.route("/useradd", methods=["POST"])
        def useradd():
            username = flask.request.form.get("username")
            password = flask.request.form.get("password")
            limit = flask.request.form.get("limit")
            client = flask.request.form.get("client")
            port = flask.request.form.get("port")
            self.adduser(username, password, limit, client, port)
            index_html = '''
            <!DOCTYPE html>
                <html>
                    <title>Hattson Server Manager</title>
                    <head>
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                        <style>
                            body{{
                                font-family: 'Alkatra', cursive;
                                font-size: 30px;
                                background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                background-repeat: no-repeat;
                                background-attachment: fixed;
                                background-size: cover;
                                color: white;
                            }}
                            button{{
                                font-family: 'Alkatra', cursive;
                                font-family: 'Tillana', cursive;
                                font-size: 30px;
                                color : white;
                                cursor: pointer;
                                outline: none;
                                border: none;
                                border-radius: 15px;
                                box-shadow: 0 9px #999;
                                background-color: transparent;
                                border: gray 2px;


                            }}


                            button:hover {{background-color: #aaafab}}

                            button:active {{
                              background-color: #3e8e41;
                              box-shadow: 0 5px #666;
                              transform: translateY(4px);
                            }}
                            #main{{
                                text-align: center;
                                margin-left: auto;
                                margin-right: auto;
                            }}

                        </style>
                    </head>
                    <body>
                        <div id='main'>
                            <h1><p>Hattson Server Manger Adding New User</p></h1>
                        </div>
                        <div id="main">
                            <p id='main'>Your user has been created successfully !</p>
                            <button class="button" onclick="window.location = '/';"> Back to menu</button>
                        </div>
                    <body>
                </html>
            '''.format()
            return index_html

        @app.route("/deluser")
        def deluser():
            user_info = self.deluser()
            for i in user_info:
                self.webDelUsers.append(i)
            last_list = []
            for (ID, user) in user_info:
                last_list.append("<tr><th>{}</th><th>{}</th></tr>".format(ID, user))
            last_list = ''.join(last_list)
            index_html = """
                        <!DOCTYPE html>
                            <html>
                                <title>Hattson Server Manager</title>
                                <head>
                                    <link rel="preconnect" href="https://fonts.googleapis.com">
                                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                                    <link rel="preconnect" href="https://fonts.googleapis.com">
                                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                                    <style>
                                        body{{
                                            font-family: 'Alkatra', cursive;
                                            font-size: 30px;
                                            background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                            background-repeat: no-repeat;
                                            background-attachment: fixed;
                                            background-size: cover;
                                            color: white;
                                        }}
                                        #main{{
                                            text-align: center;
                                            margin-left: auto;
                                            margin-right: auto;
                                        }}
                                        th{{
                                            border: 5px;
                                            border-color: #494949;
                                            border-style: groove;
                                        }}
                                        #input{{
                                            opacity: 0.3;
                                            border-radius: 15px;
                                            font-family: 'Alkatra', cursive;
                                            font-family: 'Tillana', cursive;
                                            font-size: 20px;
                                            margin-left: auto;
                                            margin-right: auto;
                                            color: black;
                                            width: 150px;
                                            height: 30px;   
                                        }}
                                        button{{
                                            font-family: 'Alkatra', cursive;
                                            font-family: 'Tillana', cursive;
                                            font-size: 30px;
                                            color : white;
                                            cursor: pointer;
                                            outline: none;
                                            border: none;
                                            border-radius: 15px;
                                            box-shadow: 0 9px #999;
                                            background-color: transparent;
                                            border: gray 2px;


                                        }}


                                        button:hover {{background-color: #aaafab}}

                                        button:active {{
                                          background-color: #3e8e41;
                                          box-shadow: 0 5px #666;
                                          transform: translateY(4px);
                                        }}
                                    </style>
                                </head>
                                <body>
                                    <div id='main'>
                                        <h1><p>Hattson Server Manger Delete Users  </p></h1>
                                    </div>
                                    <div id="main">
                                        <table id="main">
                                            <tr>
                                                <th>ID</th>
                                                <th>USERNAME</th>
                                            </tr>
                                        {}
                                        </table>
                                    </div>
                                    <div id="main">
                                        <form action='/userdel' method='post'>
                                            <div id='main'> User ID :
                                                <input id='input' name='ID' value="0" type='number'> 
                                            </div>
                                            <button class="button" type='submit' > Delete User</button>
                                        </from>
                                    </div>
                                <body>
                            </html>
                        """.format(last_list)
            return index_html

        @app.route("/userdel", methods=["POST"])
        def userdel():
            username = flask.request.form.get('ID')
            print(username)
            username = self.webDelUsers[int(username)][-1]
            print(username)
            username = username.strip().rstrip()
            self.deluser(username)
            index_html = '''
                        <!DOCTYPE html>
                            <html>
                                <title>Hattson Server Manager</title>
                                <head>
                                    <link rel="preconnect" href="https://fonts.googleapis.com">
                                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                                    <link rel="preconnect" href="https://fonts.googleapis.com">
                                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                    <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                                    <style>
                                        body{{
                                            font-family: 'Alkatra', cursive;
                                            font-size: 30px;
                                            background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                            background-repeat: no-repeat;
                                            background-attachment: fixed;
                                            background-size: cover;
                                            color: white;
                                        }}
                                        button{{
                                            font-family: 'Alkatra', cursive;
                                            font-family: 'Tillana', cursive;
                                            font-size: 30px;
                                            color : white;
                                            cursor: pointer;
                                            outline: none;
                                            border: none;
                                            border-radius: 15px;
                                            box-shadow: 0 9px #999;
                                            background-color: transparent;
                                            border: gray 2px;


                                        }}


                                        button:hover {{background-color: #aaafab}}

                                        button:active {{
                                          background-color: #3e8e41;
                                          box-shadow: 0 5px #666;
                                          transform: translateY(4px);
                                        }}
                                        #main{{
                                            text-align: center;
                                            margin-left: auto;
                                            margin-right: auto;
                                        }}

                                    </style>
                                </head>
                                <body>
                                    <div id='main'>
                                        <h1><p>Hattson Server Manger Delete User</p></h1>
                                    </div>
                                    <div id="main">
                                        <p id='main'>Your user has been deleted successfully !</p>
                                        <button class="button" onclick="window.location = '/';"> Back to menu</button>
                                    </div>
                                <body>
                            </html>
                        '''.format()
            return index_html

        @app.route('/about')
        def about():
            index_html = '''
                                    <!DOCTYPE html>
                                        <html>
                                            <title>Hattson Server Manager</title>
                                            <head>
                                                <link rel="preconnect" href="https://fonts.googleapis.com">
                                                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                                <link href="https://fonts.googleapis.com/css2?family=Alkatra&display=swap" rel="stylesheet">
                                                <link rel="preconnect" href="https://fonts.googleapis.com">
                                                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                                <link href="https://fonts.googleapis.com/css2?family=Alkatra&family=Tillana&display=swap" rel="stylesheet">
                                                <style>
                                                    body{{
                                                        font-family: 'Alkatra', cursive;
                                                        font-size: 30px;
                                                        background-image: url('http://wallpapercave.com/wp/aJ80lg2.jpg');
                                                        background-repeat: no-repeat;
                                                        background-attachment: fixed;
                                                        background-size: cover;
                                                        color: white;
                                                    }}
                                                    button{{
                                                        font-family: 'Alkatra', cursive;
                                                        font-family: 'Tillana', cursive;
                                                        font-size: 30px;
                                                        color : white;
                                                        cursor: pointer;
                                                        outline: none;
                                                        border: none;
                                                        border-radius: 15px;
                                                        box-shadow: 0 9px #999;
                                                        background-color: transparent;
                                                        border: gray 2px;


                                                    }}


                                                    button:hover {{background-color: #aaafab}}

                                                    button:active {{
                                                      background-color: #3e8e41;
                                                      box-shadow: 0 5px #666;
                                                      transform: translateY(4px);
                                                    }}
                                                    #main{{
                                                        text-align: center;
                                                        margin-left: auto;
                                                        margin-right: auto;
                                                    }}

                                                </style>
                                            </head>
                                            <body>
                                                <div id='main'>
                                                    <h1><p>Hattson Server Manger About Us</p></h1>
                                                </div>
                                                <div id="main">
                                                    <p id='main'>This application was made by Peter Hattson</p>
                                                    <p id='main'>For sending an email <a href="mailto:peterhattson@gmail.com">click here</a></p>
                                                    <p id='main'>Out github page <a href='https://github.com/PETER-HATTSON/'>click herer</a></p>

                                                    <button class="button" onclick="window.location = '/';"> Back to menu</button>
                                                </div>
                                            <body>
                                        </html>
                                    '''.format()
            return index_html

        app.run('0.0.0.0', 6000, debug=True)

    def menu(self):
        menu = consolemenu.ConsoleMenu("""
 _   _       _   _                   
| | | | __ _| |_| |_ ___  ___  _ __  
| |_| |/ _` | __| __/ __|/ _ \| '_ \ 
|  _  | (_| | |_| |_\__ \ (_) | | | |
|_| |_|\__,_|\__|\__|___/\___/|_| |_| *server manager*
               """)
        create_client_item = FunctionItem("Create new client", self.adduser)
        install_item = FunctionItem("Install", self.install)
        recover_item = FunctionItem("Recover from .database", self.recover)
        deluser_item = FunctionItem("delete a user", self.deluser)
        show_item = FunctionItem("Show client connections", self.show)
        menu.append_item(create_client_item)
        menu.append_item(install_item)
        menu.append_item(recover_item)
        menu.append_item(deluser_item)
        menu.append_item(show_item)
        menu.show()

    def install(self):
        print("installing dependencies .......")
        os.system("sudo apt update ;"
                  "suod  apt install python3;"
                  " sudo apt install python3-pip;"
                  " pip3 install console-menu;"
                  "pip3 install flask;"
                  " pip3 install crypy;"
                  " pip3 install requests ;"
                  " pip3 install python-daemon ;"
                  " sudo apt install screen ")

    def adduser(self, username='', passwordO='', period='', limit='', port=''):
        print("[*] init adding user ......")
        if not username :
            username = input("[*] Enter your username : ")
        if not passwordO:
            passwordO = input("[*] Enter your password : ")
        if not period:
            period = input("[*] Enter the time limit of the user : ")
        if not limit:
            limit = input("[*] Enter the client connection of the user : ")
        if not port :
            port = input("[*] Enter the client port : ")
            # self.portOpen(port)
        curren_time = time.ctime()

        # ip = rq.get("https://api.ipify.org?format=json").text

        out_list = [username, passwordO, curren_time, period, limit, port]
        password = crypt.crypt(passwordO, '22')
        with open('.database1', 'a+') as output:

            print(
                "[*] Confirm creating the client with  fallowing information : \nport : {}\nusername : {}"
                "\npassword : {}\n".format(port, username, passwordO))
            ask = input("[*] Are you sure for creating this user (y/n) ? ")
            if ask == "y" or ask == "Y":
                output.write("{}\n".format(out_list))
                os.system("useradd -p {} {}".format(password, username))
            else:
                print("[X] Aborting .....")
                input("[*] Hit enter to go back to the menu ...")

    def recover(self):
        input(
            "[!] Note: copy the .database file from the previous server and paste it were the server script is and hit enter .")
        with open('.database', 'r') as out:
            for line in out.readlines():
                line = line.strip()
                line = line.replace("[", '')
                line = line.replace("]", '')
                line = line.replace("'", '')
                line = line.split(',')
                print(
                    "[+] Client is recovered by the fllowing information : \nport : {}\nusername : {}\npassword : {}\n".format(
                        line[-1].strip().rstrip(), line[0].strip().rstrip(), line[1].strip().rstrip()))
                print(line)
                self.adduser(line[0].strip().rstrip(), line[1].strip().rstrip(), line[2].strip().rstrip(),
                             line[3].strip().rstrip(), line[-1].strip().rstrip())
        input("[*] Hist enter to go back to the menu")

    def deluser(self, username=""):
        if not username:
            users = []
            print("[*] finding usernames please waite ....")
            for ID in range(1000, 3000):
                try:
                    users.append(subprocess.check_output("getent passwd {}".format(ID), shell=True))
                except:
                    pass
            usernames = []
            for user in users:
                usernames.append(user.decode().split(":")[0])
            counter = 0
            returnList = []
            for user in usernames:
                counter += 1
                print("[{}] {}".format(counter, user))
                returnList.append((counter, user))
            if self.web:
                return returnList
            else:
             print("[{}] Delete all users !!! Attention there is no going back !!!".format(counter+1))
             ID = input("[*] Enter the user number : ")
             if int(ID) == counter+1:
                for user in usernames :
                    if user != "root" and user != "peter" and user != "ubuntu":
                        os.system("skill -KILL -u {}".format(user))
                        os.system("deluser --force  {}".format(user))
                        print("[+] User {} has been deleted .".format(user))
                        input("[*] Hit enter to go back to the menu .... ")
             else:
                try:
                    os.system("skill -KILL -u {}".format(usernames[int(ID) - 1]))
                    os.system("deluser --force  {}".format(usernames[int(ID) - 1]))
                    print("[+] Users where deleted successfully ")
                    input("[*] Hit enter to go back to the menu ..... ")
                except:
                    return
        if username :
            try:
                os.system("skill -KILL -u {}".format(username))
                os.system("deluser --force  {}".format(username))
                print("[+] User {} has been deleted .".format(username))
                input("[*] Hit enter to go back to the menu .... ")
            except:
                pass

    def portOpen(self):
        with open('/etc/ssh/sshd_config', 'a+') as out:
            pass
            # for line in out.readlines():
            # if "Port "+ in line

    def portClose(self):
        pass

    def show(self):
        out = subprocess.check_output(
            "lsof -i :2280,1010,2020,3030,4040,5050,6060,7070,8080,9090 -n -E|grep -v -e '->8.8.8.8'| grep -v -e '->141.95.189.14'| grep 'ESTABLISHED'|grep -v -e 'http'|grep -v -e 'xmpp-client' | grep -v -e 'tor'|cut -d' ' -f 5-100",
            shell=True)

        out = out.split(b"\n")
        out.remove(out[0])
        # print(out)
        out_splited = []
        for Out in out:
            temp = ''
            for part in Out.decode().split("IPv4")[0]:
                temp += part
            if temp not in out_splited:
                out_splited.append(temp)
        # print(out)
        # rint(out_splited)
        out_splited_2 = []
        for part in out_splited:
            out_splited_2.append(part.split("    4u")[0])
        users = []
        for user in out_splited_2:
            user = user.strip()
            user_made = ""
            for part in user.split(" ")[1:]:
                if part != " ":
                    user_made += part
            users.append(user_made)
        # for user in users:
        #        print(user)
        checked_users = []
        users_count = []
        for user in users:
            counter = 0
            if user not in checked_users:
                for number in users:
                    if number == user:
                        counter += 1
                users_count.append((user, counter))
                checked_users.append(user)
        last_list = []
        for user in users_count:
            print("[+] Username : {}\tConnections : {}".format(user[0], user[1]))
            last_list.append((user[0], user[1]))
        if not self.web:
            input("[*] Perss anything to go back to the menu ")
        if self.web:
            return last_list



# test = manager()
# test.web()
test = manager()
test.menu()
