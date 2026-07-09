async function getWeather() {
    const city = document.getElementById("cityInput").value;
    const apiKey = "3d3c932124ec73caaef6fc2e0577d37e";
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
  
    try {
      const response = await fetch(url);
      const data = await response.json();
  
      if (data.cod === "404") {
        document.getElementById("weatherResult").innerHTML = "City not found!";
        return;
      }
  
      const weather = `
        <h2>${data.name}, ${data.sys.country}</h2>
        <p>🌡 Temperature: ${data.main.temp}°C</p>
        <p>☁ Weather: ${data.weather[0].description}</p>
        <p>💨 Wind: ${data.wind.speed} m/s</p>
      `;
      document.getElementById("weatherResult").innerHTML = weather;
    } catch (error) {
      document.getElementById("weatherResult").innerHTML = "Something went wrong!";
    }
  }
  