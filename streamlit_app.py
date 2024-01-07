import streamlit as st
# import uuid
from ceval import generate_response
# from evaluation import evaluate_idea


def prob_sol():
    # st.title("Text Area Form")

    # Create a form using the st.form context manager
    with st.form("text_area_form"):
        # Add the first text area to the form
        problem = st.text_area("Enter the problem", key="text_area_1")

        # Add the second text area to the form
        solution = st.text_area("Enter your proposed solution", key="text_area_2")

        # Add a submit button to the form
        submit_button = st.form_submit_button("Submit")

    # Check if the form is submitted
    if submit_button:
        # Display the text entered in the text areas when the form is submitted
        prompt = f"""
        Here are the problem and the proposed idea as a solution:
        Problem:
        {problem.strip()}

        Solution:
        {solution.strip()}
        """ 
        # st.write("Evaluation of your idea: ", prompt)
        st.write("Evaluation of your idea: ", generate_response(prompt, "abc456", "med"))


def ceval(role):
    st.title(f"Ceval - The experts companion")

    # Clear chat history when the role is changed
    if st.session_state.get("current_role") != role:
        st.session_state.current_role = role
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can I help you", key=role):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        id = "abc345"
        name = "med"
        response = generate_response(prompt, id, name)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

def user_guide():
    st.write("## User Guide:")
    st.write("The user guide goes here!")


def main():
    PAGES = {
        "User Guide": user_guide,
        "Ceval": prob_sol,
    }

    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Select Feature", list(PAGES.keys()))

    print(choice)
    if choice == "Ceval":
        st.sidebar.markdown("### Examples of Problem/solution pair:")
        st.sidebar.markdown("Problem:")
        st.sidebar.markdown("Since the construction industry is the largest user of coal (used to fire bricks) in the country and a signficant cause of air polution, it also lead to loss of fertile topsoil. Therfore, I came up with an ingenious solution to this pertinent problem by creating bricks made from foundary dust and waste plastic.")
        st.sidebar.markdown("Solution:")
        st.sidebar.markdown("To overcome this ecological problem we came up with the bricks, made from foundary dust and waste plastic. There is no use of water in the making of these bricks. Also more water is saved during the construction process, as the walls built with these bricks don't need to be cured with water. Also the best part of this idea is that while 70 percent of the total sand can be reused, the other 30 percent, in the form of foundary dust is too fine to be used again. Also, with enhanced technology we evolve this idea in making interlocking bricks, which essentialy works like Lego blocks.")
        prob_sol()
    elif choice == "User Guide":
        user_guide()


if __name__ == "__main__":
    main()