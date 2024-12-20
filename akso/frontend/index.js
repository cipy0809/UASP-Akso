import React from 'react';
import ReactDOM from 'react-dom';

function App() {
  return (
    <div>
      <h1>Welcome to the Frontend App</h1>
      <p>This is a simple React application running in Docker.</p>
    </div>
  );
}

// Render aplikasi ke root element
ReactDOM.render(<App />, document.createElement('div'));
