# microsoft-hackathon

Overview:

With the help of GitHub Copilot written the code creating a CLI that gives us weather data of a city. The code for API call is written in python and error handling was also helped by copilot.It helped us to write codes so that we could focus more on complex parts of problem solving.

Code:

As stated in the problem statement, we have made a command line interface in python uisng argparser module. we have also use requests module to execute the api call. The OpenWeatherMap API has a unique API key for each user which is used to access the data along with other arguments in URL out of which we have used city name to get weather data in metric units. Also, as stated earlier we have used GitHub copilot for writing the code of error handling in case of wrong API call as well as for the API call itself. This has made the coding process very much easier as the main focus of the developer was on the logic of the code.

Steps to execute:

The execution of the CLI is very simple we just have to execute the following line:
python weather_report.py {city name}
for eg. python weather_report.py Delhi
