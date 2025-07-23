# Contributing to Multiple Disease Prediction System

Thank you for your interest in contributing to the Multiple Disease Prediction System! We welcome contributions from the community and are grateful for your support.

## 🤝 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs
- Describe the issue clearly with steps to reproduce
- Include system information and error messages
- Add screenshots if applicable

### Suggesting Features
- Open an issue with the label "enhancement"
- Describe the feature and its use case
- Explain how it would benefit users
- Provide mockups or examples if possible

### Code Contributions

#### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of machine learning and Streamlit

#### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/Multiple_Disease_prediction.git
   cd Multiple_Disease_prediction
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Code Style Guidelines
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes
- Keep functions small and focused

#### Testing
- Test your changes thoroughly
- Ensure all existing functionality still works
- Add tests for new features
- Test the Streamlit app locally before submitting

#### Pull Request Process
1. Update the README.md with details of changes if applicable
2. Ensure your code follows the style guidelines
3. Make sure all tests pass
4. Create a pull request with:
   - Clear title and description
   - Reference to related issues
   - Screenshots for UI changes
   - List of changes made

## 📝 Development Guidelines

### Adding New Disease Prediction Models
1. Create a new folder under the root directory
2. Include:
   - EDA notebook
   - Model training notebook
   - Trained model file (.sav)
   - Dataset (if permissible)
3. Update the main app.py to include the new model
4. Add appropriate input fields and validation
5. Update documentation

### Code Review Process
- All submissions require review before merging
- Reviewers will check for:
  - Code quality and style
  - Functionality and testing
  - Documentation updates
  - Performance implications

### Commit Message Guidelines
Use clear and meaningful commit messages:
```
feat: add new diabetes visualization
fix: resolve input validation bug
docs: update installation instructions
refactor: improve model loading efficiency
```

## 🔧 Project Structure Guidelines

When adding new files or features, follow the existing structure:
- Models and notebooks in disease-specific folders
- Main application files in the `system/` folder
- Documentation in the root directory
- Keep related files together

## 🐛 Bug Reports

When reporting bugs, include:
- Python version
- Operating system
- Streamlit version
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces

## 💡 Feature Requests

For new features, consider:
- User benefit and use case
- Implementation complexity
- Compatibility with existing features
- Performance impact
- Documentation requirements

## 📚 Documentation

Help improve documentation by:
- Fixing typos and grammar
- Adding examples and use cases
- Improving code comments
- Creating tutorials or guides
- Updating installation instructions

## 🎯 Good First Issues

New contributors can start with:
- Documentation improvements
- Adding input validation
- UI/UX enhancements
- Code refactoring
- Adding unit tests

## 📞 Getting Help

If you need help:
- Check existing issues and documentation
- Open a new issue with the "question" label
- Be specific about what you're trying to achieve

## 🙏 Recognition

Contributors will be:
- Added to the contributors list
- Mentioned in release notes
- Credited in documentation

Thank you for contributing to making healthcare prediction more accessible!

---

By contributing, you agree that your contributions will be licensed under the MIT License.
