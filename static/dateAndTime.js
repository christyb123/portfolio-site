    var x = document.getElementsByClassName("weather-list");
    var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

    startTime();


    function startTime() {
      date = new Date();
      var h = date.getHours();
      var m = date.getMinutes();
      var s = date.getSeconds();
      months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
      day = days[date.getDay()];
      theDate = [date.getDate(), months[date.getMonth()], date.getFullYear()].join(' ');

      m = checkTime(m);
      s = checkTime(s);
      document.getElementById('time').innerHTML =
      day + ' ' + theDate + ' ' + h + ":" + m + ":" + s;
      setTimeout(startTime, 500);
    }
    function checkTime(i) {
      if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
      return i;
    }
