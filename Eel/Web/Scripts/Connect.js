function Connect() {

  let succses = document.getElementById('Database')
  succses.style = 'text-align:center;color:green;'
  succses.innerHTML = '<h1>😊Database Connected</h1>'

  let host = document.getElementById("host").value;
  let user = document.getElementById("user").value;
  let password = document.getElementById("password").value;
  let port = document.getElementById("port").value;
  let database = document.getElementById("database").value;
  console.log(
    (object = {
      host: host,
      user: user,
      password: password,
      port: port,
      database: database,
    })
  );
  eel.Connect_Database(host,user,password,port,database)
  document.body.append(succses)
};
