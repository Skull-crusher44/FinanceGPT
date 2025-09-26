@echo off
echo 🚀 Setting up FinanceGPT Knowledge Base...
echo.
echo 📚 Processing comprehensive finance library:
echo    • A Random Walk Down Wall Street
echo    • The Total Money Makeover (Dave Ramsey)
echo    • The Intelligent Investor (Benjamin Graham)  
echo    • IRS Documentation
echo    • Personal Finance Guide
echo    • Investment Strategies Guide
echo.

echo � Creating financial knowledge embeddings...
python Setting_Up_vector_Store.py

echo.
echo ✅ Comprehensive knowledge base setup complete!
echo.
echo 🎯 Next steps:
echo 1. Set up your .env file with HuggingFace and Google OAuth credentials
echo 2. Run: streamlit run financebot.py
echo 3. Access your Personal Finance Assistant with expert knowledge!
echo.
pause