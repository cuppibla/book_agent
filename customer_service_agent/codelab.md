---
id: adk-eval-guide
title: Evaluating Agents with ADK
summary: Learn how to generate golden datasets and run evaluations to ensure your AI agents are trustworthy.
authors: ADK Team
duration: 20
---

# Evaluating Agents with ADK

## The Trust Gap
**Duration: 2 min**

### The Moment of Inspiration
You built a customer service agent. It works on your machine. But yesterday, it told a customer that an out-of-stock Smart Watch was available, or worse, it hallucinated a refund policy. **How do you sleep at night knowing your agent is live?**

> aside negative
> **The Problem**
> You cannot fix what you cannot measure. Without evaluation, you are flying blind.

To bridge the gap between a proof-of-concept and a production-ready AI agent, a robust and automated evaluation framework is essential. Unlike evaluating generative models, where the focus is primarily on the final output, agent evaluation requires a deeper understanding of the decision-making process.

### Your Mission Today
In this codelab, you will learn how to use ADK Eval to ensure your customer service agent is reliable and trustworthy.
✅ **Generate a Golden Dataset** using the ADK Web UI.
✅ **Understand Evaluation Configuration** and how metrics are defined.
✅ **Run an Automated Evaluation** using `adk eval`.
✅ **Run Programmatic Evaluation** using `pytest`.

#### Prerequisites
Assumes you have the current repository cloned and ADK installed.

## Step 1: Generating the Golden Dataset
**Duration: 5 min**

Before we can grade the agent, we need an answer key. In ADK, we call this the **Golden Dataset**. This dataset contains "perfect" interactions that serve as a ground truth for evaluation.

### Open the Web UI
The ADK Web UI provides an interactive way to create these golden datasets by capturing real interactions with your agent.

👉 **In your terminal, run:**
```bash
adk web
```

👉 **Open the Web UI preview** (usually at `http://localhost:8000`).

### Capture Golden Interactions
Navigate to the **Datasets** tab. Here you can see your agent's conversation history.
1.  Interact with your agent to create an ideal conversation flow, such as checking purchase history or requesting a refund.
2.  Review the conversation to ensure it represents the expected behavior.

### Export the Data
Once you are satisfied with the conversation and the trace:
👉 Click the **Generate Golden Dataset** button.

You will see a confirmation that a dataset file (e.g., `evalset780045.evalset.json`) has been saved to your repository. This file contains the raw, auto-generated trace of your conversation.

## Step 2: The Evaluation Configuration
**Duration: 3 min**

While the Web UI generates a complex `.evalset.json` file, we often want to create a cleaner, more structured test file for automated testing. We have already prepared this for you.

ADK Eval uses two main components:
1.  **Test Files**: Can be the auto-generated Golden Dataset (e.g., `customer_service_agent/evalset780045.evalset.json`) or a manually curated set (e.g., `customer_service_agent/eval.test.json`).
2.  **Config Files** (e.g., `customer_service_agent/test_config.json`): Define the metrics and thresholds for passing.

### Examine the Configuration
👉 Open `customer_service_agent/test_config.json` in your editor.

You will see a structure similar to this:
```json
{
  "criteria": {
    "tool_trajectory_avg_score": 0.8,
    "response_match_score": 0.4
  }
}
```

### Examine the Test Structure
Open `customer_service_agent/eval.test.json`. You will see cases like `product_info_check` and `refund_request`.
Each case contains:
- **User Content**: e.g., "Do you have wireless headphones in stock?"
- **Expected Tool Use**: e.g., `lookup_product_info` with arguments.
- **Final Response**: The expected natural language output.

## Step 3: Run Evaluation with ADK CLI
**Duration: 5 min**

Now it's time to run the evaluation and see how our agent performs.

### Run with Golden Dataset
You can run evaluation directly against the auto-generated golden dataset.

👉 **In your terminal, run:**
```bash
adk eval customer_service_agent customer_service_agent/evalset780045.evalset.json --config_file_path=customer_service_agent/test_config.json
```

### Run with Curated Test File
For a cleaner, more structured set of tests, you can use the manually prepared `eval.test.json`.

👉 **In your terminal, run:**
```bash
adk eval customer_service_agent customer_service_agent/eval.test.json --config_file_path=customer_service_agent/test_config.json
```

### Analyze the Results
Watch the terminal output. You will see a summary of passed and failed tests.
If a test fails, ADK provides a detailed breakdown of why, such as a mismatch in tool arguments or a response score below the threshold.

## Step 4: Run Evaluation with Pytest
**Duration: 5 min**

For CI/CD pipelines, you can run evaluations programmatically using `pytest`.

### Examine the Test Script
👉 Open `customer_service_agent/test_agent_eval.py`.
This script uses `AgentEvaluator.evaluate` to run the tests defined in `eval.test.json`.

### Run Pytest
👉 **In your terminal, run:**
```bash
pytest customer_service_agent/test_agent_eval.py
```

## Conclusion
**Duration: 2 min**

Congratulations! You have successfully evaluated your customer service agent using ADK Eval.

### What You Learned
In this codelab, you learned how to:
✅ **Generate a Golden Dataset** to establish a ground truth.
✅ **Understand Evaluation Configuration** to define success criteria.
✅ **Run Automated Evaluations** via CLI and Pytest.

By incorporating ADK Eval into your development workflow, you can build agents with confidence.
