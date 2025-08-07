# A list of some free models available on OpenRouter.ai
# For a full list, see: https://openrouter.ai/docs#models
MODELS = [
    "google/gemini-2.0-flash-exp:free", #best model
    "deepseek/deepseek-r1:free", #3rd best fallback/default
    "google/gemini-2.5-pro-exp-03-25:free",
    "openrouter/horizon-beta", #2nd best
    "tngtech/deepseek-r1t2-chimera:free",
    "deepseek/deepseek-chat-v3-0324:free"
]

# The default model to use for analysis
DEFAULT_MODEL = "openrouter/horizon-beta"
FALLBACK_MODEL = "deepseek/deepseek-r1:free"