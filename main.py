"""
Main entry point for the Legal Data Insights application.
"""
from app import app

# Run the application when executed directly
if __name__ == "__main__":
   import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT",
                                5000)),
        debug=False
    )
