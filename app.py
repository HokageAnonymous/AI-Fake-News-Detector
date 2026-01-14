import streamlit as st
import joblib
import numpy as np

# --------------------------------------------
# Page Setup
# --------------------------------------------
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Fake News Detector")
st.markdown("Enter any news headline or paragraph below and the AI model will classify it as **Real** or **Fake**.")

# --------------------------------------------
# Load Model & Vectorizer
# --------------------------------------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("lr_model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
        return model, vectorizer
    except Exception as e:
        st.error(f"❌ Error loading model/vectorizer: {e}")
        return None, None

model, vectorizer = load_model()

# --------------------------------------------
# Example Snippets
# --------------------------------------------
with st.expander("Try an example"):
    st.write("Click to insert an example text:")
    col1, col2 = st.columns(2)
    if col1.button("Politics News"):
        st.session_state["input_text"] = "\"U.S., North Korea clash at U.N. arms forum on nuclear threat\",\"GENEVA \"\n\"(Reuters) - North Korea and the United States accused each other on Tuesday of posing a nuclear threat, with Pyongyang s envoy declaring it would never put its atomic arsenal up for negotiation. The debate at the United Nations began when the U.S. envoy said President Donald Trump s top priority was to protect the United States and its allies against the  growing threat  from North Korea. To do so, he said, the country was ready to use  the full range of capabilities at our disposal . U.S. Ambassador Robert Wood told the Conference on Disarmament that the  path to dialogue still remains an option  for Pyongyang, but that Washington was  undeterred in defending against the threat North Korea poses . Fears have grown over North Korea s development of missiles and nuclear weapons since Pyongyang test-launched intercontinental ballistic missiles (ICBMs) in July. Those fears worsened after Trump warned that North Korea would face  fire and fury  if it threatened the United States. His remarks led North Korea to say it was considering plans to fire missiles towards the U.S. Pacific territory of Guam. Trump responded by tweeting that the U.S. military was  locked and loaded, should North Korea act unwisely . A few days later, North Korean media reported the country s leader, Kim Jong Un, had delayed any decision on whether to fire missiles towards Guam while he waited to see what the United States would do. Experts warned Pyongyang could still go ahead with the missile launches.      North Korea s ballistic missile and nuclear weapons programs pose grave threats to the entire world,  Wood told the Geneva forum.  Its recent ICBM tests are another example of the dangerous reckless behavior of the North that is destabilizing the region and beyond.  North Korea had openly stated that its missiles are intended to strike cities in the United States and its allies South Korea and Japan, he said.  My president s top priority remains protecting the homeland, U.S. territories and our allies against North Korean aggression. We remain prepared to use the full range of capabilities at our disposal against the growing threat from North Korea.  North Korea diplomat Ju Yong Chol said that measures taken by his country to strengthen its nuclear deterrent and develop inter-continental rockets were  justifiable and a legitimate option .  As long as the U.S. hostile policy and nuclear threat remains unchallenged, the DPRK will never place its self-defensive nuclear deterrence on the negotiating table or step back an inch from the path it took to bolster the national nuclear force,  Ju said. In a subsequent speech, Ju said:  The United States should clearly understand that military threats and pressure are only serving as a momentum that pushes the DPRK further into developing fully strengthened nuclear deterrence.  Regarding joint U.S.-South Korean military exercises that began on Monday, he said:  The ongoing military adventure would certainly add gasoline to the fire, driving the current tense situation to further deterioration.  China s disarmament ambassador, Fu Cong, called for support for its proposal to defuse the crisis affecting its Pyongyang ally.  China has called for  dual suspension , that is of North Korea s nuclear activities and joint military exercises between the Republic of Korea and United States. This seeks to denuclearize the peninsula and promote a security mechanism.  Wood rejected Beijing s  freeze for freeze  plan.  This proposal unfortunately creates a false equivalency between states that are engaging in legitimate exercises of self-defense who have done so for many years with a regime that has basically violated countless Security Council resolutions with regard to its proscribed nuclear and ballistic missile programs,  he told the gathering.  That is a false equivalency that we cannot accept and will not accept,  he said. Fu retorted:  I just want to say that we re not creating equivalency between anything. We are just actually making the proposal to facilitate a dialogue and to reduce the tension. We need a starting point to really launch the dialogue.  \""
    if col2.button("Fake Clickbait"):
        st.session_state["input_text"] = " Donald Trump’s Eating Habits Could Be Dramatically Affecting His Wellbeing And Our Safety,\"We ve all heard the stories of Donald Trump preferring a well-done steak with ketchup and shunning any new delicacies, despite living a lifestyle that offers him all the luxuries one could ever desire, however, it s not just that the President has terrible gastronomical taste, a new memoir suggests that his diet is one of several poor lifestyle choices that could very well shorten his life.According to an excerpt from Let Trump be Trump, an upcoming book by Trump s former campaign manager Corey Lewandowski and aide David Bossie, we get to enter the inner circle where the President of the United States having a 2,400-calorie McDonald s dinner is par for the course. Trump s appetite seems to know no bounds when it comes to McDonald s, with a dinner order consisting of two Big Macs, two Filet-O-Fish, and a chocolate malted,  is just one of the claims made in the book. To put that meal in perspective, Trump s dinner contains 3,400 grams of sodium, despite the American Heart Foundation recommending just 1,500 grams per day, plus enough white bread to last most people a week. Remember, this is just one meal, but it only gets worse. On Trump Force One there were four major food groups: McDonald s, Kentucky Fried Chicken, pizza, and Diet Coke,  the authors write about traveling with Trump during the early days of his presidency, but there may be a valid reason for it   Not only is he a fan of manufacturing, Trump is also a renowned germaphobe who allegedly won t eat from a package that has already been opened, which would also explain the plane s cupboards being stacked with Vienna Fingers, potato chips, pretzels, and many packages of Oreos.  Those well-done steaks make a little more sense now, as well. But a little bit of bacteria is probably the least of the President s worries. This is a 71-year-old man who gets next to no exercise (it s hard to include his golf when he barely even walks while playing), gets very little sleep, and is constantly throwing tantrums, so add in that diet and you have the perfect recipe for a heart attack. The diet alone, especially the snacks, is almost an open-invite for diabetes, too.What makes this frightening for the rest of us is that this is a man who is currently responsible for a nuclear standoff with North Korea, as well as dealing with rapidly warming oceans and an ever-increasing tax bill. If he has this lack of concern for his own wellbeing, then what does it say of his risk-assessment abilities?Featured image via Win McNamee/Getty Images\",News,\"December 5,2017\""
# --------------------------------------------
# Text Input Box
# --------------------------------------------
input_text = st.text_area(
    label="📝 News Text:",
    placeholder="Paste or type news article text here...",
    height=200,
    key="input_text"
)

# --------------------------------------------
# Prediction Logic
# --------------------------------------------
if st.button("Analyze"):
    if not input_text.strip():
        st.warning("⚠ Please enter some text before analyzing.")
    else:
        clean_text = input_text.lower().strip()
        converted = vectorizer.transform([clean_text])

        prediction = model.predict(converted)[0]
        prob = model.predict_proba(converted)[0]
        confidence = np.max(prob) * 100

        # Display results
        if prediction == 1:
            st.success(f"✔️ **REAL NEWS**")
        else:
            st.error(f"❌ **FAKE NEWS**")

        st.write(f"**Confidence:** {confidence:.2f}%")

# --------------------------------------------
# Footer
# --------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning & Streamlit")
