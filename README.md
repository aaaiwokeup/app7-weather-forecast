# Weather Forecast Application

This project is a web application built using Streamlit to display weather forecasts for a specified location. It uses the OpenWeatherMap API to fetch weather data for a given city and allows users to visualize the forecasted temperature or sky conditions for the upcoming days.

## Features

1. **User Input**: The application allows users to input a city name and select the number of forecast days (1 to 5).
2. **Forecast Options**: Users can choose to display either the temperature or sky conditions for the forecasted days.
3. **Visualizations**:
   - A line chart displays the temperature forecast.
   - Images (e.g., clear, clouds, rain, snow) represent the sky conditions.
4. **Dynamic Headers**: The application dynamically updates headers based on the selected number of forecast days.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   API_KEY=your_openweathermap_api_key
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the URL displayed in your terminal (usually `http://localhost:8501`) to access the application.
3. Enter the city name in the input box and select the desired forecast days.
4. Choose a forecast category (“Temperature” or “Sky”) and view the results.

## Code Structure

### `app.py`
- The main Streamlit application.
- Handles user inputs, displays data, and visualizations.
- Fetches weather data using the `get_data` function from the `backend` module.

### `backend.py`
- Contains the `get_data` function to interact with the OpenWeatherMap API.
- Filters and processes weather data based on user inputs.

## API Integration
The application uses the OpenWeatherMap API for fetching weather data. Ensure you have a valid API key added to your `.env` file. The API returns data in JSON format, which is processed and displayed in the application.

## Example

1. Enter `Kyiv` as the city name.
2. Select 3 forecast days.
3. Choose the “Temperature” category.
4. View a line chart showing the temperature forecast for the next 3 days.
5. Alternatively, choose the “Sky” category to view images representing the sky conditions.

## Dependencies

- `streamlit`
- `plotly`
- `requests`
- `python-dotenv`

## Notes

- Make sure your API key has access to the OpenWeatherMap 5-day/3-hour forecast API.
- The application uses Streamlit's session state to store and manage user inputs.

## Future Improvements

- Add more weather metrics, such as wind speed or humidity.
- Enhance the UI/UX with more interactive elements.
- Include error handling for invalid city names or API issues.

