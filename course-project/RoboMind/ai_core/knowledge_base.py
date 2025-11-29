"""
Knowledge Base - Logic Reasoning Module
SE444 - Artificial Intelligence Course Project

Implemented propositional logic knowledge base with inference
Phase 2 (Week 3-4)
"""

from typing import Set, List


class KnowledgeBase:
    """
    A simple knowledge base for propositional logic.
    
    Stores facts and rules, performs forward chaining inference.
    """
    
    def __init__(self):
        """Initialize empty knowledge base."""
        self.facts = set()   # Known facts: "Safe(2,3)", "Obstacle(4,5)"
        self.rules = []      # Rules: ("A", "B", "C") means "A AND B → C"
    
    def tell(self, fact: str):
        """
        Add a fact to the knowledge base.
        
        Args:
            fact: A proposition like "Safe(2,3)" or "Explored(5,6)"
        
        Example:
            >>> kb = KnowledgeBase()
            >>> kb.tell("Safe(2,3)")
            >>> kb.tell("Free(2,3)")
        """
        if fact not in self.facts:
            self.facts.add(fact)
            # Automatically trigger inference when new facts are added
            self.infer()
    
    def add_rule(self, premises: List[str], conclusion: str):
        """
        Add an inference rule.
        
        Args:
            premises: List of propositions that must all be true
            conclusion: Proposition that follows from premises
        
        Example:
            >>> kb.add_rule(["Safe(X)", "Free(X)"], "CanMove(X)")
            This means: If Safe(X) AND Free(X) then CanMove(X)
        """
        self.rules.append((premises, conclusion))
    
    def ask(self, query: str) -> bool:
        """
        Check if a query can be inferred from the knowledge base.
        
        Args:
            query: A proposition to check
        
        Returns:
            True if query is known or can be inferred, False otherwise
        
        Example:
            >>> kb.ask("Safe(2,3)")
            True
        """
        return query in self.facts
    
    def infer(self):
        """
        Apply forward chaining to derive new facts from rules.
        
        Forward chaining:
            1. For each rule: check if all premises are satisfied
            2. If yes, add conclusion to facts
            3. Repeat until no new facts can be derived
        
        Example:
            >>> kb.tell("Safe(2,3)")
            >>> kb.tell("Free(2,3)")
            >>> kb.add_rule(["Safe(2,3)", "Free(2,3)"], "CanMove(2,3)")
            >>> kb.infer()
            >>> kb.ask("CanMove(2,3)")
            True
        """
        changed = True
        while changed:
            changed = False
            for premises, conclusion in self.rules:
                # Check if all premises are in facts and conclusion is not
                if all(premise in self.facts for premise in premises) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    changed = True
    
    def clear_facts(self):
        """Clear all facts but keep rules."""
        self.facts.clear()
    
    def get_facts(self) -> Set[str]:
        """Get all current facts."""
        return self.facts.copy()
    
    def get_rules(self) -> List:
        """Get all rules."""
        return self.rules.copy()
    
    def __str__(self) -> str:
        """String representation of KB."""
        facts_str = "\n  ".join(sorted(self.facts))
        rules_str = "\n  ".join([f"{' AND '.join(premises)} → {conclusion}" 
                               for premises, conclusion in self.rules])
        return f"Knowledge Base:\nFacts ({len(self.facts)}):\n  {facts_str}\nRules ({len(self.rules)}):\n  {rules_str}"
