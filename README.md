# Computational Analysis of Voting Mechanisms in Social Choice Theory

## Introduction

Voting mechanisms are fundamental in social choice theory and multi-agent decision making. 
Different voting rules can produce different outcomes even when voters have the same preferences.

This project implements and compares several classical voting algorithms and analyzes how their results differ through computational simulations.

## Voting Algorithms Implemented

1. **Plurality Voting**
   - Each voter selects one candidate.
   - The candidate with the most votes wins.

2. **Borda Count**
   - Candidates receive points based on ranking position.
   - Higher ranked candidates receive more points.

3. **Condorcet Method**
   - A candidate who beats every other candidate in pairwise comparisons is the winner.

## Condorcet Paradox

The project also detects the **Condorcet Paradox**, a situation where collective preferences become cyclic:

A preferred over B  
B preferred over C  
C preferred over A  

This means no clear winner exists even though majority preferences exist for each pair.

## Experimental Setup

The simulation runs multiple elections with randomly generated voter preferences.

- Number of voters: 50
- Number of candidates: 4
- Number of elections simulated: 100

Each simulation compares the results produced by different voting mechanisms.

## Results

The program records:

- Frequency of winners under different voting rules
- Cases where voting rules disagree
- Occurrences of the Condorcet paradox

These results illustrate how different voting mechanisms can produce different outcomes even with the same voter preferences.

## Technologies Used

- Python
- Matplotlib
- Random preference simulation


The program will simulate elections and display the results along with graphical analysis.

## Future Work

Possible extensions include:

- More voting rules (Instant Runoff, Approval Voting)
- Strategic voting simulations
- Multi-agent preference modeling
