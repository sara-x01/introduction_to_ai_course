"""
Bayesian Reasoning Module
SE444 - Artificial Intelligence Course Project

TODO: Implement Bayesian belief updates for handling uncertainty
Phase 3 (Week 5-6)
"""

from typing import Dict, Tuple


def bayes_update(prior: float, likelihood: float, evidence: float) -> float:
    """
    Update belief using Bayes' Rule.
    
    Bayes' Rule:
        P(H|E) = P(E|H) * P(H) / P(E)
    
    Where:
        - P(H|E) = posterior probability (what we want to compute)
        - P(E|H) = likelihood (probability of evidence given hypothesis)
        - P(H) = prior probability (initial belief)
        - P(E) = evidence probability (normalization factor)
    
    Args:
        prior: P(Hypothesis) - our initial belief
        likelihood: P(Evidence|Hypothesis) - how likely we see this evidence if H is true
        evidence: P(Evidence) - overall probability of seeing this evidence
    
    Returns:
        posterior: P(Hypothesis|Evidence) - updated belief
    
    Example:
        Sensor detects obstacle with 90% accuracy.
        Prior belief cell is blocked: 0.3
        Sensor says "blocked"
        
        >>> P_H = 0.3              # prior: 30% believe it's blocked
        >>> P_E_given_H = 0.9      # likelihood: if blocked, 90% sensor says blocked
        >>> P_E = 0.3*0.9 + 0.7*0.1  # evidence: total prob of "blocked" reading
        >>> posterior = bayes_update(P_H, P_E_given_H, P_E)
        >>> print(f"Updated belief: {posterior:.2f}")  # ~0.79 (79%)
    """
    if evidence == 0:
        return prior #bc prior is the belief before seeing the evidence, we can't say return 1/0 here bc it means that the hypothesis is T/F and we don't know that without evidence 
    posterior = (likelihood * prior) / evidence
    return posterior

def compute_evidence(prior: float, likelihood_h: float, likelihood_not_h: float) -> float:
    """
    Compute total probability of evidence P(E) using law of total probability.
    
    P(E) = P(E|H)*P(H) + P(E|¬H)*P(¬H)
    
    Args:
        prior: P(H)
        likelihood_h: P(E|H)
        likelihood_not_h: P(E|¬H)
    
    Returns:
        P(E): Total probability of evidence
    
    Example:
        >>> P_E = compute_evidence(0.3, 0.9, 0.1)
        >>> print(f"P(evidence) = {P_E:.3f}")  # 0.34
    """
    # TODO: Implement law of total probability
    raise NotImplementedError("Evidence computation not implemented yet!")


def update_belief_map(belief_map: Dict[Tuple[int, int], float],
                      sensor_reading: bool,
                      sensor_accuracy: float = 0.9) -> Dict[Tuple[int, int], float]:
    """
    Update entire grid belief map based on sensor reading.
    
    Sensor Model:
        - If cell has obstacle:
            P(sensor says "obstacle" | obstacle exists) = sensor_accuracy (e.g., 0.9)
        - If cell is free:
            P(sensor says "obstacle" | no obstacle) = 1 - sensor_accuracy (e.g., 0.1)
    
    Args:
        belief_map: Dictionary mapping (row, col) -> probability of obstacle
        sensor_reading: True if sensor detects obstacle, False otherwise
        sensor_accuracy: Probability sensor is correct (default 0.9)
    
    Returns:
        updated_belief_map: Updated probabilities for each cell
    
    Example:
        >>> beliefs = {(0,0): 0.5, (0,1): 0.3, (1,0): 0.7}
        >>> sensor_says_obstacle = True
        >>> updated = update_belief_map(beliefs, sensor_says_obstacle, 0.9)
    """
    # TODO: Implement belief map update
    #
    # For each cell:
    #   1. Get prior belief
    #   2. Compute likelihood based on sensor reading and accuracy
    #   3. Compute evidence (total probability)
    #   4. Apply Bayes' rule to get posterior
    #   5. Store updated belief
    
    raise NotImplementedError("Belief map update not implemented yet!")


def sensor_model(actual_state: bool, sensor_accuracy: float = 0.9) -> Tuple[float, float]:
    """
    Define the sensor model probabilities.
    
    Args:
        actual_state: True if obstacle exists, False if free
        sensor_accuracy: Accuracy of sensor
    
    Returns:
        (P(sensor=True|state), P(sensor=False|state))
    
    Example:
        >>> P_true, P_false = sensor_model(actual_state=True, sensor_accuracy=0.9)
        >>> print(f"If obstacle exists: P(detect)={P_true}, P(miss)={P_false}")
    """
    # TODO: Implement sensor model
    if actual_state:  # obstacle exists
        return sensor_accuracy, 1 - sensor_accuracy
    else:  # no obstacle
        return 1 - sensor_accuracy, sensor_accuracy


# ============================================================================
# Testing Code
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  Testing Bayesian Reasoning")
    print("=" * 60 + "\n")
    
    print("Example: Medical diagnosis")
    print("-" * 40)
    print("Disease prevalence: 1% (P(Disease) = 0.01)")
    print("Test accuracy: 95% (P(+|Disease) = 0.95)")
    print("False positive: 10% (P(+|Healthy) = 0.10)")
    print("\nPatient tests positive. What's the probability they have the disease?")
    
    try:
        # Prior
        P_disease = 0.01
        P_healthy = 1 - P_disease
        
        # Likelihood
        P_pos_given_disease = 0.95
        P_pos_given_healthy = 0.10
        
        # Evidence
        P_pos = compute_evidence(P_disease, P_pos_given_disease, P_pos_given_healthy)
        
        # Posterior
        P_disease_given_pos = bayes_update(P_disease, P_pos_given_disease, P_pos)
        
        print(f"\nResult: P(Disease|+) = {P_disease_given_pos:.1%}")
        print("(Surprisingly low despite positive test!)")
        
    except NotImplementedError:
        print("\n⚠️  Bayes' rule not implemented yet!")
    
    print("\n" + "=" * 60)
    print("  Example: Robot Sensor")
    print("=" * 60)
    print("\nRobot sensor is 90% accurate")
    print("Prior belief cell has obstacle: 30%")
    print("Sensor detects obstacle")
    print("\nWhat's updated belief?")
    
    try:
        P_obstacle = 0.30
        P_detect_if_obstacle = 0.90
        P_detect_if_free = 0.10
        
        P_detect = compute_evidence(P_obstacle, P_detect_if_obstacle, P_detect_if_free)
        P_obstacle_given_detect = bayes_update(P_obstacle, P_detect_if_obstacle, P_detect)
        
        print(f"\nResult: P(Obstacle|Detected) = {P_obstacle_given_detect:.1%}")
        print(f"Belief increased from {P_obstacle:.1%} to {P_obstacle_given_detect:.1%}")
        
    except NotImplementedError:
        print("\n⚠️  Bayes' rule not implemented yet!")
    
    print("\n💡 Tip: Start with the basic bayes_update() function,")
    print("   then build up to belief maps!")

