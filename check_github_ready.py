#!/usr/bin/env python3
"""
GitHub Preparation Status Checker
"""

import os


def check_file_exists(filepath, description):
    """Check if a file exists and print status"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - MISSING")
        return False


def main():
    """Main function to check project readiness"""
    print("🔍 GitHub Preparation Status Check")
    print("=" * 50)

    required_files = [
        ("README.md", "Main documentation"),
        ("requirements.txt", "Python dependencies"),
        ("LICENSE", "License file"),
        (".gitignore", "Git ignore file"),
        ("CONTRIBUTING.md", "Contributing guidelines"),
        ("CHANGELOG.md", "Change log"),
        ("DEPLOYMENT.md", "Deployment guide"),
        ("Dockerfile", "Docker configuration"),
        ("docker-compose.yml", "Docker Compose configuration"),
        (".github/workflows/ci-cd.yml", "CI/CD pipeline"),
        ("system/app.py", "Main application"),
        ("tests/test_app.py", "Test suite"),
    ]

    model_files = [
        ("system/diabetes_trained_model.sav", "Diabetes model"),
        ("system/heart_trained_model.sav", "Heart disease model"),
        ("system/parkinson_trained_model.sav", "Parkinson's model"),
    ]

    all_good = True

    print("\n📄 Required Files:")
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_good = False

    print("\n🤖 Model Files:")
    for filepath, description in model_files:
        if not check_file_exists(filepath, description):
            all_good = False

    print("\n📊 Project Structure:")
    directories = ["Diabetes", "Heart", "Parkinson", "system", "tests", ".github"]
    for directory in directories:
        if os.path.isdir(directory):
            print(f"✅ Directory: {directory}")
        else:
            print(f"❌ Directory: {directory} - MISSING")
            all_good = False

    print("\n" + "=" * 50)
    if all_good:
        print("🎉 Project is ready for GitHub!")
        print("\nNext steps:")
        print("1. Initialize git: git init")
        print("2. Add files: git add .")
        print("3. Commit: git commit -m 'Initial commit'")
        print("4. Create GitHub repository")
        print("5. Add remote: git remote add origin <your-repo-url>")
        print("6. Push: git push -u origin main")
    else:
        print("⚠️  Some files are missing. Please review the list above.")

    print("\n📋 Additional Recommendations:")
    print("- Update README.md with your GitHub username")
    print("- Replace placeholder email addresses")
    print("- Add screenshots to README.md")
    print("- Test the application locally before pushing")
    print("- Consider adding more comprehensive tests")


if __name__ == "__main__":
    main()
