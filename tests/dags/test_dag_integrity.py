import glob
from os import path
import pytest
import importlib.util
from airflow import models as airflow_models
from airflow.utils.dag_cycle_tester import test_cycle as _test_cycle


DAG_PATH = glob.glob(
    path.join(path.dirname(__file__), "..", "..", "dags", "*.py")
)


@pytest.mark.parametrize("dag_path", DAG_PATH)
def teste_dag_integrity(dag_path):
    dag_name = path.basename(dag_path)
    module = _import_file(dag_name, dag_path)

    dag_obj = [
        var
        for var in vars(module).values()
        if isinstance(var, airflow_models.DAG)
    ]
    assert dag_obj

    for dag in dag_obj:
        _test_cycle(dag)


def _import_file(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, str(module_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    pytest.main([__file__])
