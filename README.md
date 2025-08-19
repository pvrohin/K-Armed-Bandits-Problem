# K-Armed Bandit Problem

## Overview

This repository contains an implementation of the **k-armed bandit problem**, a fundamental concept in reinforcement learning and decision-making under uncertainty. The project demonstrates different exploration strategies and their impact on learning optimal actions.

## What is the K-Armed Bandit Problem?

The k-armed bandit problem is a classic problem in probability theory and reinforcement learning where:

- You have **k different actions** (arms) to choose from
- Each action has an unknown, fixed reward distribution
- Your goal is to **maximize total reward** over time
- You must balance **exploration** (trying different actions) vs **exploitation** (choosing the best-known action)

Think of it like choosing between k slot machines (bandits) in a casino, where you want to maximize your winnings but don't know which machine pays the most.

## Problem Setup

In this implementation:
- **k = 10** (10 different arms/actions)
- Each arm has a **normal distribution** with:
  - Mean: 0.0
  - Variance: 1.0
- **Time horizon**: 1000 steps
- **Number of runs**: 2000 (for statistical significance)

## Exploration Strategies

The code implements and compares three different exploration strategies:

1. **ε = 0.0** (Pure Exploitation)
   - Always chooses the action with highest estimated value
   - No exploration, may get stuck in local optima

2. **ε = 0.01** (Low Exploration)
   - 1% chance of random exploration
   - 99% chance of choosing best-known action
   - Balanced approach

3. **ε = 0.1** (High Exploration)
   - 10% chance of random exploration
   - 90% chance of choosing best-known action
   - More exploration, potentially better long-term performance

## Implementation Details

### Key Components

- **Q-values**: Estimated value of each action
- **Action counts**: Number of times each action has been taken
- **Reward tracking**: Average rewards over time for each strategy
- **Optimal action tracking**: Percentage of times the best action was chosen

### Algorithm

For each time step:
1. Generate reward for all arms based on their distributions
2. Decide whether to explore (random choice) or exploit (best Q-value)
3. Select an action and receive reward
4. Update Q-value using incremental averaging
5. Track performance metrics

## Results

The implementation generates two key visualizations:

1. **Average Reward Over Time**
   - Shows how total reward accumulates for each strategy
   - Helps understand which approach maximizes long-term gains

2. **Percentage of Optimal Actions**
   - Shows how often each strategy chooses the best action
   - Indicates learning effectiveness

## Files

- `assignment_2.py`: Main implementation file
- `Assignment-2.pdf`: Assignment details and requirements
- `README.md`: This documentation file

## Requirements

```bash
pip install numpy matplotlib
```

## Usage

Simply run the Python script:

```bash
python assignment_2.py
```

This will execute the simulation and display the results as two matplotlib plots.

## Key Insights

- **Exploration vs Exploitation Trade-off**: The ε-greedy strategy balances these competing objectives
- **Learning Rate**: Q-values are updated incrementally, allowing for continuous learning
- **Statistical Significance**: Multiple runs ensure robust performance evaluation
- **Performance Metrics**: Both reward accumulation and action optimality are important measures

## Applications

The k-armed bandit problem has real-world applications in:
- **A/B Testing**: Testing different website designs or features
- **Clinical Trials**: Testing different medical treatments
- **Recommendation Systems**: Suggesting products or content
- **Resource Allocation**: Distributing limited resources optimally
- **Online Advertising**: Choosing which ads to display

## Learning Outcomes

This implementation demonstrates:
- **Reinforcement Learning Fundamentals**: Value estimation and policy improvement
- **Exploration Strategies**: Different approaches to the exploration-exploitation dilemma
- **Statistical Learning**: Incremental updates and convergence
- **Performance Analysis**: Multiple metrics for evaluating learning algorithms

## Future Enhancements

Potential improvements could include:
- **UCB (Upper Confidence Bound)** strategy
- **Thompson Sampling** approach
- **Contextual Bandits** with state information
- **Non-stationary environments** where reward distributions change over time
- **More sophisticated exploration strategies**

---

*This project serves as an excellent introduction to reinforcement learning concepts and decision-making under uncertainty.*