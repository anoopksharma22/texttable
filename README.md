Prints the csv file in tabular form

Examples:

demo.csv
```
Serial No,First Name,Last Name,Address
1,Frank R.,Lapointe,938 Hampton Meadows Lowell MA 01852
2,Terri J.,Roberge,4503 Yorkshire Circle Gatesville NC 27938
3,Anastazja,Sobczak,ul. Kaktusowa 72 85-485 Bydgoszcz
```

```python ./cmd/main.py -f demo.csv```

output
```
----------------------------------------------------------------------------------
| Serial No | First Name | Last Name | Address                                   |
----------------------------------------------------------------------------------
| 1         | Frank R.   | Lapointe  | 938 Hampton Meadows Lowell MA 01852       |
----------------------------------------------------------------------------------
| 2         | Terri J.   | Roberge   | 4503 Yorkshire Circle Gatesville NC 27938 |
----------------------------------------------------------------------------------
| 3         | Anastazja  | Sobczak   | ul. Kaktusowa 72 85-485 Bydgoszcz         |
----------------------------------------------------------------------------------
```

## Run web app
```
python app.py
```

```
$ python app.py 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.100:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 346-683-403
 ```
 
 Environment variables like host port debug etc defined in `.env file`
