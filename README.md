## Flask Application Design for A Engineer MBTI Dating APP

### HTML Files

- **index.html**: Landing page displaying a form for users to select their MBTI type and engineer specialty.
- **results.html**: Presents a list of potential matches based on the user's MBTI type and engineer specialty.

### Routes

- ** / **: Handles GET requests for the landing page and renders the 'index.html' file.
- ** /select **: Handles POST requests from the form on the landing page. Extracts the MBTI type and engineer specialty from the form and stores them in a session variable. Redirects to the '/results' route.
- ** /results **: Handles GET requests to display the results page. Retrieves the MBTI type and engineer specialty from the session variable and uses that information to query a database or API for potential matches. Renders the 'results.html' file with the list of matches.

### Additional Considerations

- The application should include a database or integration with an API to store and retrieve MBTI data and engineer specialties.
- The 'results.html' template should allow users to view detailed profiles of potential matches.
- The application should have basic error handling in place to handle any potential issues.