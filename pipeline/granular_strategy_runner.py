from pipeline.tools.strategy_navigator import StrategyNavigator

class GranularStrategyRunner():
    
    @classmethod
    def runStrategy(cls, strategy_type: str, module_name: str, text: str) -> str:
        strategy = StrategyNavigator.get_concrete_strategy_class(strategy_type, module_name)
        return strategy.execute(text)

    