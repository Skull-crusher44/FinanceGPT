# Test script to verify your finance book collection
import os

def check_finance_books():
    """Check what finance books are available in the data directory"""
    data_path = "data/"
    
    print("🏦 FinanceGPT Knowledge Base Inventory")
    print("=" * 50)
    
    # Check for files
    if os.path.exists(data_path):
        files = os.listdir(data_path)
        
        pdfs = [f for f in files if f.endswith('.pdf')]
        txts = [f for f in files if f.endswith('.txt')]
        
        print(f"\n📚 PDF Books ({len(pdfs)}):")
        for pdf in pdfs:
            size = os.path.getsize(os.path.join(data_path, pdf)) / (1024*1024)
            print(f"   ✅ {pdf} ({size:.1f} MB)")
        
        print(f"\n📄 Text Guides ({len(txts)}):")
        for txt in txts:
            size = os.path.getsize(os.path.join(data_path, txt)) / 1024
            print(f"   ✅ {txt} ({size:.1f} KB)")
        
        total_files = len(pdfs) + len(txts)
        print(f"\n🎯 Total Knowledge Sources: {total_files}")
        
        if total_files >= 5:
            print("✅ Excellent! Comprehensive finance library ready")
        elif total_files >= 3:
            print("👍 Good collection! Ready for knowledge base creation")
        else:
            print("⚠️  Consider adding more finance books for better coverage")
            
    else:
        print("❌ Data directory not found!")

if __name__ == "__main__":
    check_finance_books()