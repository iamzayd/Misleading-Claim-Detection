import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Informed Investing", page_icon="💼")
st.sidebar.markdown('''
Created with 💜 by [Najeeb](https://www.instagram.com/thiscloudbook/) And [Karthik](https://www.instagram.com/_mr_thop/).
''')


# Title section with styling
st.title("Misleading Claims in Investment Content")
st.markdown("---")

# Stylish content section
st.markdown(
    """
    Misleading claims in investment content are a serious problem. They can lead investors to make bad decisions that could cost them money.
    
    Here are some common examples of misleading claims:
    
    - **"This investment is guaranteed to make you rich."**
    - **"This investment is risk-free."**
    - **"This investment is backed by the government."**
    - **"This investment is only available for a limited time."**
    
    If you see any of these claims, be skeptical. Do your own research before investing any money. """)



image_url = "https://img.washingtonpost.com/news/get-there/wp-content/uploads/sites/37/2016/08/0819_cash2_ss.gif"

  # Display the image
st.image(image_url, caption="(Washington Post Illustration; iStock)", use_column_width=True, width = 100)


st.subheader("Learn more about misleading claims")

st.markdown("""
    
    
    
    Here are some resources where you can learn more about misleading claims in investment content:
    - [The Economic Times On Misleading Investors](https://economictimes.indiatimes.com/topic/misleading-claim-by-investors)
    - [Misleading Investors](https://cafemutual.com/news/industry/28695-sebi-cracks-down-heavily-on-so-called-influencers)
    """
)
st.markdown("---")

# Stylish button for further learning
if st.button("📚 Learn more about Informed Investing"):
    st.markdown(
        """
        If you're new to investing, check out these articles:
        - [The Ultimate Guide to Investing](https://www.thebalancemoney.com/the-ultimate-guide-to-investing-in-india-1979063)
        - [Investing Education](https://www.investopedia.com/)
        - [Smart Investing](https://www.nasdaq.com/smart-investing)
        """
    )

