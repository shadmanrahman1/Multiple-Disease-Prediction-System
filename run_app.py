#!/usr/bin/env python3
"""
Multiple Disease Prediction System Launcher
"""

import os
import sys
import subprocess
import argparse


def check_requirements():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import numpy
        import sklearn

        print("✅ All required packages are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False


def run_app(port=8501, host="localhost"):
    """Run the Streamlit application"""
    if not check_requirements():
        sys.exit(1)

    app_path = os.path.join("system", "app.py")

    if not os.path.exists(app_path):
        print(f"❌ Application file not found: {app_path}")
        sys.exit(1)

    print(f"🚀 Starting Multiple Disease Prediction System...")
    print(f"🌐 URL: http://{host}:{port}")
    print("📱 The application will open in your default browser")
    print("⏹️  Press Ctrl+C to stop the application")

    try:
        subprocess.run(
            [
                "streamlit",
                "run",
                app_path,
                "--server.port",
                str(port),
                "--server.address",
                host,
            ]
        )
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install: pip install streamlit")
        sys.exit(1)


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Multiple Disease Prediction System Launcher"
    )
    parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8501,
        help="Port to run the application on (default: 8501)",
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to run the application on (default: localhost)",
    )

    args = parser.parse_args()

    print("🏥 Multiple Disease Prediction System")
    print("=" * 50)

    run_app(port=args.port, host=args.host)


if __name__ == "__main__":
    main()
