import streamlit as st

st.set_page_config(layout="wide")  # Set the page layout to wide

col9, col10 = st.columns([0.5, 5])  # Adjust the width ratios as needed

with col9 :
     st.image("logo.png",width=75)  # Replace with the path to your logo

with col10:
     st.write("## Paani Waali Data")

st.sidebar.markdown('''
Created with 💜 by [Najeeb](https://www.instagram.com/thiscloudbook/) And [Karthik](https://www.instagram.com/_mr_thop/).
''')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.write("\n")
st.write("\n")
st.write("Welcome to the realm where technology synergizes with your vigilance, possibilities unfold. With our AI model as your steadfast ally, you're not just a user – you're an integral part of a collective effort. Together, we navigate the intricate terrain of the digital world armed with cutting-edge analysis and shared determination.")
st.write("As you delve into this realm, your interactions shape its evolution. Your inputs, your discernment, and your quest for authenticity fuel a community-driven pursuit of truth. Our AI model stands as a testament to the power of collaboration, unifying technology and human insight.")
st.write("As you enter this space, every action you take becomes a catalyst for precision. Each report you make reinforces the bastion of credibility. With our AI model as your guide, embark on an unparalleled digital adventure – where empowerment blossoms from collective resilience. This is your digital odyssey, and you hold the key to a future fortified by collaboration.")


st.write("---")


st.write(" In today's information-rich world, accurate data is critical for informed decision-making. We, as a team of passionate engineering students, are excited to present our Data Integrity Project.")

st.header("Our Mission")
st.write("Our mission is to tackle the issue of misleading data. We've developed a platform that empowers users to analyze content, identify misleading information, and contribute to reporting data inaccuracies.")

st.header("Project Highlights")
st.write("Our project highlights include:")
st.write("✅ Claiming Misleading Data: Uncovering and addressing misleading information.")
st.write("🔍 Analyzing Content: Providing tools to analyze content and comments for data integrity.")
st.write("🚩 Reporting/Flagging Data: Enabling users to report and flag inaccurate data.")
st.write("🌐 Cloud Computing: Leveraging cloud technology for seamless data processing.")

st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')

st.write("---")

st.write('  ')
st.write('  ')
st.write('  ')
st.write('  ')

col1, col2 = st.columns(2)


with col1:
        # Load and display the image on the left side
        image_path = "3.jpg"  # Replace with the actual path to your image
        st.image(image_path, width=400)

with col2:
        st.header("Empower Your Digital Journey with Us")
        st.write('  ')
        st.write('  ')


        st.write("Our platform stands as your unwavering companion in the quest for reliable information. Amid the vast ocean of digital content, envision us as your guiding compass, steering you toward credible content creators while providing a shield against the tide of misleading narratives. You hold a pivotal role in this journey – your vigilant reporting and data flagging directly nurture a safer online ecosystem.With cutting-edge AI technology, our platform plunges into the depths of YouTube videos and Reddit posts, meticulously unearthing their authenticity. As you embark on this digital expedition, rest assured that your pursuit of truth is fortified by our commitment to accuracy and integrity. Whether you're dissecting a video's credibility or scrutinizing a Reddit thread, our tools empower you to make informed choices in an intricate digital world.Together, we shape a realm where transparency thrives, where the collective actions of users like you dismantle the foundations of misinformation. As our AI technology delves deep, your discernment acts as the anchor for a trustworthy online voyage. With each click and contribution, you sculpt a digital landscape of certainty – a place where misinformation dissolves, and credibility reigns. ")

st.write("---")


st.header(" How to access our Platform and get the best out of it " )

st.write('  ')
st.write('  ')
st.write('  ')

col4, col5, col6 = st.columns(3)

with col4:
        st.subheader("Differentiating")
        st.write("Unveiling the Truth: Mastering Our Content Differentiation Feature")
        st.write("Navigate the content-rich digital landscape with precision using our unique differentiation feature. Here's your guide to effortlessly distinguish between misleading narratives and authentic content:\n\n"
                 "1. *Credibility Scans:* Our AI technology rigorously scans content sources, assessing credibility based on multiple parameters. Look for the 'Credibility Score' to quickly assess content reliability.\n"
                 "2. *Creator Insights:* Discover insights about content creators. Verify their track record, engagement, and authenticity to ensure you engage with trustworthy sources.\n"
                 "3. *Fact-Check Tools:* Unmask misinformation by utilizing our fact-checking tools. Evaluate claims and cross-reference information to make informed decisions.\n"
                 "4. *Visual Integrity:* Our platform visually represents content analysis results. Graphs, charts, and color-coded indicators provide instant clarity on content authenticity.\n\n"
                 "With these tools at your fingertips, you're empowered to navigate the digital realm, knowing you can confidently differentiate between genuine content and misleading narratives. Elevate your online experience today.")



with col5:
        st.subheader("Analyzing")
        st.write("Unlocking Insights: A Guide to Analyzing Content")
        st.write("Embark on a journey of digital discernment with our content analysis feature. Here's how to leverage its power to decode the authenticity of YouTube videos and Reddit posts:\n\n"
                 "1. *Paste and Analyze:* Copy and paste the link of the content you want to analyze. Our AI technology takes over, dissecting the information for credibility.\n"
                 "2. *Depth of Evaluation:* Our analysis goes beyond surface-level. It examines metadata, sources, context, and engagement patterns to provide a comprehensive authenticity assessment.\n"
                 "3. *Credibility Insights:* Gain insights into the content's credibility, backed by data-driven metrics. Our platform empowers you to make decisions based on reliable information.\n"
                 "4. *User Vigilance:* While AI drives analysis, your vigilance is essential. Flag and report questionable content to strengthen our collective defense against misleading narratives.\n\n"
                 "Experience the empowerment of analyzing content like a pro. With our tools and your discernment, you're equipped to navigate the digital landscape, uncovering the truth beneath the surface.")


with col6:
        st.subheader("Reporting")
        st.write("Strengthening Digital Integrity: How to Report Suspicious Content")
        st.write("Play a crucial role in maintaining digital authenticity by reporting and flagging questionable content. Here's your guide to contributing to a safer online environment:\n\n"
                 "1. *Identify Suspicion:* Trust your instincts. If content seems misleading, suspicious, or false, it's worth investigating further.\n"
                 "2. *Use the Reporting Feature:* Within our platform, find the reporting tool. Provide details about the content and why you find it concerning.\n"
                 "3. *User-Curated Insights:* Your insights matter. By sharing your perspective, you contribute to collective vigilance, creating a safer digital space for everyone.\n"
                 "4. *Empower Action:* Your reports enable prompt action. Our team investigates flagged content to determine its authenticity and take necessary measures.\n\n"
                 "Join the effort to ensure online integrity. With your active participation, we can counteract the spread of misleading information and fortify the digital landscape.")


st.write("---")
st.write("  ")
st.write('  ')
st.write('  ')
st.write('  ')

col7,col8=st.columns(2)

with col7:
     image_path = "3.png"  # Replace with the actual path to your image
     st.image(image_path, width=450 )

with col8:
     st.header(" Heart of our Platform  :  ")
     st.write("At the heart of our platform lies a game-changing AI model, meticulously trained to uphold online authenticity. Here's a closer look at how our AI technology transforms your digital journey:  \n \n"
              "1.*Sophisticated Analysis* :  Our AI dives deep into content, scrutinizing metadata, language, and context. It discerns patterns and anomalies, offering insights beyond human capability.\n"
              "2.*Misinformation Detection*: Armed with a vast knowledge base, our AI detects misinformation cues, cross-referencing against trusted sources to validate or debunk claims.\n"
              "3.*Evolving Accuracy*: The more it learns, the smarter it gets. Our AI model continuously evolves, adapting to emerging trends and deceptive tactics in the digital landscape.\n"
              "4.*User Collaboration*: You're not just a bystander – your interactions refine our AI's understanding. User-flagged content contributes to continuous improvement, making our model a collective effort.\n"
              "5.*Instant Insights* : Within seconds, our AI analyzes social media content, presenting you with an authenticity score and insights, empowering you to make informed choices.\n"
     )


st.write("---")

col9, col10 = st.columns([0.5, 5])  # Adjust the width ratios as needed
