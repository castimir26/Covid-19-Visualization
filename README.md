# Covid-19-Visualization
A Covid-19 Data Visualization application using React, Bootstrap4 and Chart.js, powered by Python and Django. Data comes from John Hopkins University.

This has been a stretch project for me. For one thing, it was my first real usage of React. I find the templating language used in
Django to be cumbersome, so I wanted to use a modern, dedicated frontend framework. I created the React app as a separate Django app
within the larger project and passed a RESTful api from the database to React. I think this is cleanlier than other methods of combining
React and Django.

Currently the functionality is simple. Covid-19 data is displayed by country and province (if all are available) as selected in a search bar.
I have the world totals displayed as well. I am adding chart functionality using ChartJS.

Next steps:
1). Better exception handling. I am currently running into problems with how Django and React interact with exceptions. I need to add a lot
more exception handling so diagnosing bugs doesn't take as long and the react app recovers more gracefully.

2). Implement charts by country and province, if available, that display once a country has been selected.

3). Replace search bar with dropdown menu.

4). Setup country to country comparisons

5). Calculate other ratios, such as recovery to confirmed case ratios and death percentages. Break down by country and province, as available.
