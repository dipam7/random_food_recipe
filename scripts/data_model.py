from typing import List
from pydantic import BaseModel, Field

class FoodRecipe(BaseModel):
    title: str = Field(..., description="The title of the recipe")
    ingredients: List[str] = Field(..., description="List of ingredients required for the recipe")
    cooking_instructions: str = Field(..., description="Step by step cooking instructions")
    cook_time_minutes: int = Field(..., description="Cooking time in minutes")
    cuisine: str = Field(None, description="Cuisine of the recipe")
    is_vegan: bool = Field(..., description="Is the recipe vegan?")
    tags: List[str] = Field([], description="Tags related to the recipe for easy searching")