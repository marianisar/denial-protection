# zemanata

Requirments:
------------
    Install python(2.7 or above)


Run Application:
----------------
    1)open your terminal and run below command to start server.
        python server.py

    2)Now open seocnd terminal and run below command.
        python client.py

        This will ask you to enter the number of HTTP clients to simulate and number must be integer and greater than
        zero.it will simulate the N number of clienst(1->N).client ids will be in range from 1 to n.

    3)Now send as many requests you want to send(with in range of number of clients you simulated).5 request per 5 sec
     will be processed againts each client.

     e.g: http://localhost:8080/?clientId=n

    4)If you want to stop any client at any time press key to stop (ctrl C) any client request otherwise it will run infinitely.

    NOTE:
         Server must be run before running "client.py"
