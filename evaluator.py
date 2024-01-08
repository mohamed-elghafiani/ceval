from openai import OpenAI
client = OpenAI()

prompt1 = """
You will be given a problem along with a circular economy business model as a solution. Your task is to evaluate the solution based on multiple metrics. Please explain the rating based on the criteria given and give a numerical value from 1 to 10, 1 being the worst and 10 being the best. Please also number the evaluation criteria and highlight these criteria. Note that if the problem and/or solution are sloppy, off-topic, unsuitable, or vague, refrain from rating it.
Evaluation Criteria:
Please evaluate the solution from 0 to 10 based on the following criteria:
1. Maturity Stage:
   - Assess the current development stage of the circular economy solution.
   - Consider factors such as research, testing, and implementation phases.
   - Provide a numerical rating and explain your reasoning.

2. Market Potential:
   - Evaluate the solution's potential success in the market.
   - Consider target audience, demand, competition, and market trends.
   - Provide a numerical rating and explain your reasoning.

3. Feasibility:
   - Examine the practicality and viability of implementing the solution.
   - Assess resource requirements, timeframes, and potential obstacles.
   - Provide a numerical rating and explain your reasoning.

4. Scalability:
   - Evaluate the ability of the solution to scale effectively.
   - Consider expansion possibilities, adaptability, and growth prospects.
   - Provide a numerical rating and explain your reasoning.

5. Technological Innovation:
   - Assess the level of technological advancement and innovation in the solution.
   - Consider any cutting-edge technologies incorporated.
   - Provide a numerical rating and explain your reasoning.
6. Adherence to Circular Economy Principles:
   - Evaluate how well the solution aligns with circular economy principles.
   - Consider factors like resource efficiency, waste reduction, and closed-loop systems.
   - Provide a numerical rating and explain your reasoning.

Evaluation Steps:
1. Read the problem and the solution carefully and identifies the main idea and the key points of the proposed solution in relation to the problem.
2. Conduct a thourough assessment of the solution and consolidate the findings from the individual assessments LCA, Extended IOA, MFA, Emergy, Exergy to generate a comprehensive overall evaluation. Consider the interplay between environmental impact, economic implications, and adherence to circular economy principles.
3. Assign a final holistic score on a scale of 1 to 10, providing a well-documented and justified assessment.

Evaluation Form (Answer by starting with "Analysis:" to analyze the given example regarding the evaluation criteria as concise as possible, and then give the numeric rating on the next line by "Rating:):
- {Attribute}:
"""

prompt2 = """
You will be given a problem along with a circular economy business model as a solution. Your task is to evaluate the solution based on multiple metrics. Please explain the rating based on the criteria given and give a numerical value from 1 to 10, 1 being the worst and 10 being the best. Please also number the evaluation criteria and highlight these criteria. Note that if the problem and/or solution are sloppy, off-topic, unsuitable, or vague, refrain from rating it.

Evaluation Criteria:
Please evaluate the solution from 0 to 10 based on the following criteria:
1. Maturity Stage:
   - Assess the current development stage of the circular economy solution.
   - Consider factors such as research, testing, and implementation phases.
   - Provide a numerical rating and explain your reasoning.

2. Market Potential:
   - Evaluate the solution's potential success in the market.
   - Consider target audience, demand, competition, and market trends.
   - Provide a numerical rating and explain your reasoning.

3. Feasibility:
   - Examine the practicality and viability of implementing the solution.
   - Assess resource requirements, timeframes, and potential obstacles.
   - Provide a numerical rating and explain your reasoning.

4. Scalability:
   - Evaluate the ability of the solution to scale effectively.
   - Consider expansion possibilities, adaptability, and growth prospects.
   - Provide a numerical rating and explain your reasoning.

5. Technological Innovation:
   - Assess the level of technological advancement and innovation in the solution.
   - Consider any cutting-edge technologies incorporated.
   - Provide a numerical rating and explain your reasoning.
 
6. Adherence to Circular Economy Principles:
   - Evaluate how well the solution aligns with circular economy principles.
   - Consider factors like resource efficiency, waste reduction, and closed-loop systems.
   - Provide a numerical rating and explain your reasoning.

Evaluation Steps:
1. Read the problem and the solution carefully and identifies the main idea and the key points of the proposed solution in relation to the problem.
2. Conduct a thourough assessment of the solution and consolidate the findings from the individual assessments LCA, Extended IOA, MFA, Emergy, Exergy to generate a comprehensive overall evaluation. Consider the interplay between environmental impact, economic implications, and adherence to circular economy principles.
3. Assign a final holistic score on a scale of 1 to 10, providing a well-documented and justified assessment.

Evaluation Form (Answer by starting with
"Rating:" and then give the explanation
of the rating on the next line by "Rationale:"):
- {Attribute}:
"""

prompt3 = """
 You will be given a problem along with a circular economy business model as a solution. Your task is to evaluate the solution based on multiple metrics. Please explain the rating based on the criteria given and give a numerical value from 1 to 10, 1 being the worst and 10 being the best. Please also number the evaluation criteria and highlight these criteria. Note that if the problem and/or solution are sloppy, off-topic, unsuitable, or vague, refrain from rating it.

Evaluation Criteria:
Please evaluate the solution from 0 to 10 based on the following criteria:
1. Maturity Stage:
   - Assess the current development stage of the circular economy solution.
   - Consider factors such as research, testing, and implementation phases.
   - Provide a numerical rating and explain your reasoning.

2. Market Potential:
   - Evaluate the solution's potential success in the market.
   - Consider target audience, demand, competition, and market trends.
   - Provide a numerical rating and explain your reasoning.

3. Feasibility:
   - Examine the practicality and viability of implementing the solution.
   - Assess resource requirements, timeframes, and potential obstacles.
   - Provide a numerical rating and explain your reasoning.

4. Scalability:
   - Evaluate the ability of the solution to scale effectively.
   - Consider expansion possibilities, adaptability, and growth prospects.
   - Provide a numerical rating and explain your reasoning.

5. Technological Innovation:
   - Assess the level of technological advancement and innovation in the solution.
   - Consider any cutting-edge technologies incorporated.
   - Provide a numerical rating and explain your reasoning. 
6. Adherence to Circular Economy Principles:
   - Evaluate how well the solution aligns with circular economy principles.
   - Consider factors like resource efficiency, waste reduction, and closed-loop systems.
   - Provide a numerical rating and explain your reasoning.

Evaluation Steps:
1. Read the problem and the solution carefully and identifies the main idea and the key points of the proposed solution in relation to the problem.
2. Conduct a thourough assessment of the solution and consolidate the findings from the individual assessments LCA, Extended IOA, MFA, Emergy, Exergy to generate a comprehensive overall evaluation. Consider the interplay between environmental impact, economic implications, and adherence to circular economy principles.
3. Assign a final holistic score on a scale of 1 to 10, providing a well-documented and justified assessment.
"""

super_prompt = """
You will be provided with three different evaluations for a circular economy business model solution, each assessed based on various criteria and assigned numerical scores from 1 to 10. Your task is to analyze these three evaluations and arrive at the final decision. Please follow the steps below:

1. Evaluate Individual Assessments:
   - Review the three evaluations, each conducted based on criteria such as Maturity Stage, Market Potential, Feasibility, Scalability, Technological Innovation, and Adherence to Circular Economy Principles.
   - Examine the provided numerical scores and rationales for each criterion in all three evaluations.

3. Final Holistic Score:
   - Based on your analysis, assign a final holistic score on a scale of 1 to 10 for the circular economy business model solution.
   - Provide a well-documented and justified assessment, highlighting key insights and considerations from the individual evaluations and the consolidated analysis.

Note: Ensure that the final score and rationale are derived by averaging and synthesizing the information from the three evaluations to offer the most comprehensive and informed decision.

Evaluation Form (Answer by starting with
"Rating:" and then give the explanation
of the rating on the next line by "Rationale:"):
- {Attribute}:
"""


problem = '' #problem here
solution = '' #solution here

def evaluator(problem, solution):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": prompt1 + '\n' + f"problem: {problem}" + '\n' + f"solution: {solution}"},
        {"role": "user", "content": prompt2 + '\n' + f"problem: {problem}" + '\n' + f"solution: {solution}"},
        {"role": "user", "content": prompt3 + '\n' + f"problem: {problem}" + '\n' + f"solution: {solution}"}
        ]
    )

    eval1 = completion.choices[0].message #string containing response for prompt1
    eval2 = completion.choices[1].message
    eval3 = completion.choices[2].message
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": super_prompt + f'Here is the first evaluation:\n{eval1}' \
        + f'Here is the second evaluation:\n{eval2}' + f'Here is the third evaluation:\n{eval3}'
      },
    ]
    )
    
    finalEval = completion.choices[0].message

    return finalEval
