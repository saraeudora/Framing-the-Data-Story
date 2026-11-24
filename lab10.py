
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Lab 10 | Framing the Data Story",
    layout="wide"
)

st.title("Lab 10: Framing the Data Story")

st.markdown(
    "### Audience-Focused Data Visualization"
)

st.write(
    "This dashboard presents students' self-rated data "
    "visualization skills to help workshop instructors "
    "identify areas requiring additional teaching support."
)

# ==========================================
# DATA
# ==========================================

skills = [
    "Data storytelling",
    "Python",
    "Chart selection",
    "Color and labels",
    "Data cleaning"
]

ratings = [2.4, 2.1, 3.2, 3.7, 4.1]

df = pd.DataFrame({
    "Skill": skills,
    "Average rating": ratings
})

# Identify lowest-rated skill
lowest_index = df["Average rating"].idxmin()
lowest_skill = df.loc[lowest_index, "Skill"]
lowest_rating = df.loc[lowest_index, "Average rating"]

# ==========================================
# SECTION 1: AUDIENCE AND PURPOSE
# ==========================================

st.header("1. Audience and Purpose")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Target Audience")
    st.write(
        "Workshop instructors responsible for planning "
        "data visualization workshops."
    )

with col2:
    st.subheader("Purpose")
    st.write(
        "Identify students' weaker data visualization "
        "skills and determine which areas require "
        "additional teaching support."
    )

st.subheader("Key Takeaway")

st.info(
    f"{lowest_skill} received the lowest average "
    f"self-rating of {lowest_rating:.1f} out of 5. "
    "Therefore, the next workshop should prioritise "
    f"{lowest_skill} to provide additional learning support."
)

# ==========================================
# SECTION 2: DATA VISUALIZATION
# ==========================================

st.header("2. Students' Data Visualization Skills")

st.write(
    "The chart compares students' average self-ratings "
    "across five data visualization skills."
)

fig, ax = plt.subplots(figsize=(9, 5))

# Highlight the lowest-rated skill
bar_colors = [
    "#E07A3F" if i == lowest_index else "#4C78A8"
    for i in range(len(skills))
]

bars = ax.barh(
    df["Skill"],
    df["Average rating"],
    color=bar_colors,
    height=0.6
)

ax.set_xlim(0, 5)
ax.set_xticks(range(0, 6))

ax.set_xlabel(
    "Average self-rating (1 = beginner, 5 = confident)"
)

ax.set_title(
    f"{lowest_skill} Received the Lowest Average Self-Rating",
    pad=15,
    fontweight="bold"
)

ax.invert_yaxis()

ax.grid(
    axis="x",
    color="#DDDDDD",
    linewidth=0.7
)

ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Numerical labels
for i, bar in enumerate(bars):
    value = ratings[i]

    ax.text(
        value + 0.08,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center",
        fontweight="bold" if i == lowest_index else "normal"
    )

# Annotation
highlighted_bar = bars[lowest_index]

ax.annotate(
    "Needs more practice",
    xy=(
        lowest_rating,
        highlighted_bar.get_y() + highlighted_bar.get_height() / 2
    ),
    xytext=(3.0, highlighted_bar.get_y() + 0.15),
    arrowprops=dict(
        arrowstyle="->",
        color="#E07A3F",
        linewidth=1.2
    ),
    color="#C45F2A",
    fontsize=9,
    fontweight="bold"
)

fig.tight_layout()

st.pyplot(fig, clear_figure=True)

st.caption(
    "Source: Fictional practice data. Values represent "
    "average student self-ratings on a scale of 1 to 5."
)

# ==========================================
# SECTION 3: IMPROVEMENTS MADE
# ==========================================

st.header("3. Improvements Made")

st.write(
    "The original chart was modified to communicate "
    "the findings more effectively to workshop instructors."
)

improvements = pd.DataFrame({
    "Element": [
        "Target audience",
        "Python rating",
        "Highlighted skill",
        "Chart title",
        "Explanatory annotation"
    ],
    "Modification": [
        "Students → Workshop instructors",
        "3.0 → 2.1",
        "Data storytelling → Python",
        "Updated to focus on Python",
        "Added 'Needs more practice'"
    ]
})

st.table(improvements)

st.write(
    "The Python rating was changed from 3.0 to 2.1, "
    "making it the lowest-rated skill. The chart title "
    "and orange highlight were updated to match the "
    "new finding. An explanatory annotation was also "
    "added to emphasise the area requiring more practice."
)

# ==========================================
# SECTION 4: EVALUATION AND FEEDBACK
# ==========================================

st.header("4. Evaluation and Feedback")

st.write(
    "The chart should be shown to a classmate without "
    "explaining the takeaway beforehand."
)

st.markdown("**Questions for the classmate:**")

st.markdown(
    """
    1. What do the axes represent?
    2. What does the highlighted orange bar indicate?
    3. What should the workshop instructor remember?
    """
)

st.markdown("**Feedback Record**")

understood = st.text_area(
    "One point the classmate understood:",
    placeholder="Record the actual response from your classmate..."
)

unclear = st.text_area(
    "One point that was unclear:",
    placeholder="Record what your classmate found difficult to understand..."
)

revision = st.text_area(
    "Revision made based on feedback:",
    placeholder="Describe how you improved the chart or explanation..."
)

# ==========================================
# SECTION 5: SHORT REPORT
# ==========================================

st.header("5. Short Report")

with st.expander("View Short Report", expanded=True):

    st.subheader("Audience and Purpose")

    st.write(
        "The target audience for this data visualization "
        "is workshop instructors who are responsible for "
        "planning data visualization workshops. The purpose "
        "is to help instructors identify students' weaker "
        "data visualization skills and determine which "
        "areas require additional teaching support."
    )

    st.subheader("Key Takeaway")

    st.write(
        f"{lowest_skill} received the lowest average "
        f"self-rating of {lowest_rating:.1f} out of 5, "
        "followed by data storytelling at 2.4. Therefore, "
        f"{lowest_skill} should be prioritised in the next "
        "workshop to help students improve their skills."
    )

    st.subheader("Improvements Made")

    st.write(
        "The original chart was modified by changing the "
        "Python rating from 3.0 to 2.1. This made Python "
        "the lowest-rated skill instead of data storytelling. "
        "The chart title and highlighted bar were updated "
        "accordingly. An orange colour was used to highlight "
        "Python, while the remaining bars retained their blue "
        "colour. An explanatory annotation, 'Needs more "
        "practice', was also added to emphasise the main finding."
    )

    st.subheader("Evaluation and Feedback")

    st.write(
        "The chart was evaluated by showing it to a classmate "
        "without explaining its takeaway beforehand. Feedback "
        "was collected to assess whether the axes, highlighted "
        "bar and main message were understood."
    )

    if understood or unclear or revision:
        st.markdown("**Classmate Feedback**")
        if understood:
            st.write("Understood:", understood)
        if unclear:
            st.write("Unclear:", unclear)
        if revision:
            st.write("Revision:", revision)
    else:
        st.warning(
            "Complete the feedback record after evaluating "
            "the chart with a classmate."
        )

# ==========================================
# SECTION 6: REFLECTION
# ==========================================

st.header("6. Reflection")

reflection = """
Visual emphasis and explanatory text play an important
role in helping audiences understand and remember the
main message of a data visualisation. In this lab, I used
a contrasting orange colour to highlight Python, which
received the lowest average self-rating of 2.1 out of 5.
The remaining skills were displayed in blue to create a
clear visual distinction. This use of colour helps direct
the audience's attention towards the most important
finding without requiring them to compare every bar
individually.

Additionally, the chart title, numerical labels and
explanatory annotation provide context for interpreting
the results. The title communicates the main finding,
while the annotation, "Needs more practice", explains
why Python deserves attention. The axis label also
clarifies that the values represent average self-ratings
on a scale of 1 to 5.

Classmate feedback can help identify areas where the
explanation could be clearer, particularly regarding
the meaning of the average ratings. Overall, combining
visual emphasis with clear explanations reduces
unnecessary information, improves understanding and
helps the audience retain the key takeaway.
"""

with st.expander("View Reflection", expanded=True):
    st.write(reflection)

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "TFB3133/TEB3133 Data Visualization | Lab 10: "
    "Framing the Data Story | September 2026"
)
