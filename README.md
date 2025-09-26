# 💰 FinanceGPT – AI-Powered Personal Finance Assistant

FinanceGPT is an intelligent financial chatbot powered by a comprehensive library of finance classics and expert knowledge. Get personalized advice on budgeting, investing, debt management, and financial planning from the wisdom of financial legends like Benjamin Graham, Dave Ramsey, and Burton Malkiel.

---

## 📚 **Expert Knowledge Base**

Our AI is trained on authoritative finance literature:

### 📖 **Classic Finance Books**
- **"The Intelligent Investor"** by Benjamin Graham - Warren Buffett's favorite investment guide
- **"A Random Walk Down Wall Street"** by Burton Malkiel - Index investing and market efficiency  
- **"The Total Money Makeover"** by Dave Ramsey - Debt elimination and budgeting mastery

### 🏛️ **Official Resources**
- **IRS Documentation** - Authoritative tax planning and optimization strategies
- **Custom Investment Strategies Guide** - Comprehensive portfolio management
- **Personal Finance Guide** - Fundamental financial planning principles

### 🎯 **What This Means For You**
- Get advice backed by **decades of proven financial wisdom**
- Access insights from **millionaire-making strategies**
- Receive guidance based on **government tax resources**
- Learn from **Nobel Prize-winning economic research**

---

## 📊 Financial Planning Tools

### 🧮 Interactive Calculators
- **Compound Interest Calculator** - Visualize investment growth over time
- **Retirement Planning Calculator** - Determine savings needed for retirement
- **Debt Payoff Calculator** - Compare debt avalanche vs snowball strategies  
- **Emergency Fund Calculator** - Calculate emergency fund requirements
- **Investment Risk Calculator** - Analyze potential investment scenarios

### 💡 AI-Powered Financial Advice
Ask questions about:
- 💰 **Budgeting Strategies** - 50/30/20 rule, zero-based budgeting, expense tracking
- 📈 **Investment Planning** - Asset allocation, diversification, risk management
- 💳 **Debt Management** - Payoff strategies, credit score improvement
- 🏖️ **Retirement Planning** - 401(k) optimization, IRA strategies, withdrawal planning
- 🛡️ **Insurance & Risk** - Life, health, disability, and property insurance guidance
- 📋 **Tax Planning** - Tax-advantaged accounts, deductions, tax strategies

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- HuggingFace API Token (free)
- Google OAuth credentials (for authentication)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/FinanceGPT.git
   cd FinanceGPT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   HF_TOKEN=your_huggingface_token
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```

4. **Create the knowledge base**
   ```bash
   python create_memory_for_llm.py
   ```

5. **Run the application**
   ```bash
   streamlit run financebot.py
   ```

---

## 🎯 Usage Examples

### Financial Planning Questions
- "How should I allocate my investment portfolio at age 30?"
- "What's the difference between Roth and Traditional IRA?"
- "How much should I save for an emergency fund?"
- "Should I pay off debt or invest first?"
- "How do I create a budget that actually works?"

### Calculator Usage
- **Compound Interest**: See how $500/month grows over 30 years
- **Retirement Planning**: Calculate if you're on track for retirement
- **Debt Payoff**: Compare avalanche vs snowball debt strategies
- **Emergency Fund**: Determine adequate emergency fund size

---

## 🔧 Configuration

### Knowledge Base Customization
Add your own financial documents to the `data/` directory:
- Personal finance books (PDF or TXT)
- Investment guides
- Financial planning resources
- Tax planning documents

Then regenerate the knowledge base:
```bash
python create_memory_for_llm.py
```

### Authentication Setup
1. Create a Google Cloud project
2. Enable Google+ API
3. Create OAuth 2.0 credentials
4. Add authorized redirect URIs
5. Update `.env` file with credentials

---

## 📁 Project Structure

```
FinanceGPT/
├── financebot.py                 # Main Streamlit application
├── finance_calculators.py        # Financial planning calculators
├── create_memory_for_llm.py      # Knowledge base creation
├── connect_memory_with_llm.py    # Standalone chat interface
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version
├── .env                         # Environment variables (create this)
├── auth/
│   └── google_oauth.py          # Google OAuth implementation
├── data/
│   ├── Personal_Finance_Guide.txt
│   └── Investment_Strategies_Guide.txt
└── vectorstore/
    └── db_faiss/               # FAISS vector database
        ├── index.faiss
        └── index.pkl
```

---

## 🤝 Contributing

We welcome contributions! Here are ways you can help:

1. **Add Financial Content** - Contribute high-quality financial guides
2. **Improve Calculators** - Add new financial planning tools
3. **Enhance UI/UX** - Improve the user interface and experience
4. **Bug Fixes** - Report and fix issues
5. **Documentation** - Improve setup and usage guides

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## ⚠️ Important Disclaimers

- **Not Professional Financial Advice**: This tool provides educational information only
- **Consult Professionals**: Always consult qualified financial advisors for personalized advice
- **No Investment Recommendations**: Information provided is for educational purposes only
- **Risk Awareness**: All investments carry risk; past performance doesn't guarantee future results

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Support

- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Join community discussions in GitHub Discussions
- **Documentation**: Check the wiki for detailed guides

---

## 🌟 Acknowledgments

- HuggingFace for providing excellent LLM infrastructure
- Streamlit for the amazing web framework
- LangChain for RAG implementation tools
- The open-source community for financial education resources

---

**Built with ❤️ for financial literacy and empowerment**