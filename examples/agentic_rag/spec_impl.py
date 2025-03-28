"""This file was generated using `langgraph-gen` version 0.0.6.

This file provides a placeholder implementation for the corresponding stub.

Replace the placeholder implementation with your own logic.
"""

from typing_extensions import TypedDict

from spec import AgenticRag


class SomeState(TypedDict):
    # define your attributes here
    foo: str


# Define stand-alone functions
def agent(state: SomeState) -> dict:
    print("Node: agent (NOT IMPLEMENTED)")
    return {
        # Add your state update logic here
    }


def retrieve(state: SomeState) -> dict:
    print("Node: retrieve (NOT IMPLEMENTED)")
    return {
        # Add your state update logic here
    }


def rewrite(state: SomeState) -> dict:
    print("Node: rewrite (NOT IMPLEMENTED)")
    return {
        # Add your state update logic here
    }


def generate(state: SomeState) -> dict:
    print("Node: generate (NOT IMPLEMENTED)")
    return {
        # Add your state update logic here
    }


def is_relevant(state: dict) -> str:
    """Condition for retrieve → rewrite, generate"""
    print("Edge Condition: is_relevant (NOT IMPLEMENTED)")
    print("\n  Available paths:")
    paths = ["rewrite", "generate", ]
        
    for i, path in enumerate(paths, 1):
        print(f"  {i}. {path}")
            
    while True:
        try:
            choice = int(input("\n  Select a path (enter number): "))
            if 1 <= choice <= len(paths):
                return paths[choice - 1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

agent = AgenticRag(
    state_schema=SomeState,
    impl=[
        ("agent", agent),
        ("retrieve", retrieve),
        ("rewrite", rewrite),
        ("generate", generate),
        ("is_relevant", is_relevant),
    ],
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
