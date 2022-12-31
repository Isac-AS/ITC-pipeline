import pkgutil
import inspect

class StrategyNavigator:
    """
    Auxiliary tool to list and retrieve strategy class references.
    This tool will be used to update the context reference to one strategy.
    """
    
    @classmethod
    def list_strategies(cls) -> list:
        """
        Lists the different strategy types that constitute the pipeline.

        :return: List containing the package names of the different strategies used
        :rtype: list
        """
        strategies = [module_info.name for module_info in pkgutil.iter_modules([f"pipeline_strategies"]) if module_info.ispkg]
        return strategies

    @classmethod
    def list_concrete_strategies(cls, strategy_type: str) -> list:
        """
        List the implemented strategies within a strategy type. 
        For example, can list the implemented spell checking strategies.

        :param strategy_type: Desired strategy type to expand
        :type strategy_type: str
        :return: List containing the module names of the implemented strategies
        :rtype: list
        """
        concrete_strategies = [module_info.name for module_info in pkgutil.iter_modules([f"pipeline_strategies/{strategy_type}"])]
        return concrete_strategies

    @classmethod
    def get_concrete_strategy_class(cls, strategy_type: str, module_name:str):
        """
        Fetches a reference to a concrete strategy.
        As the strategies' execute method is a classmethod, it can be called directly from the reference.

        :param strategy_type: Desired strategy type
        :type strategy_type: str
        :param module_name: Concrete module within the strategy type
        :type module_name: str
        :return: Class reference to the strategy
        :rtype: class
        """
        module_info = [module_info for module_info in pkgutil.iter_modules([f"pipeline_strategies/{strategy_type}"]) if module_info.name == module_name][0]
        spec = module_info.module_finder.find_spec(module_info.name)
        module = spec.loader.load_module()
        clsmembers = inspect.getmembers(module, inspect.isclass)
        for _, class_reference in clsmembers:
            if class_reference.__module__.split(".")[-1] == module_name:
                return class_reference
        return "Module not found"
        