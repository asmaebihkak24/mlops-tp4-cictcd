from src.data import load_params
from src.train import train


def test_model_quality_gate():
    params = load_params()
    _, metrics = train()

    assert metrics["accuracy"] >= params["quality_gate"]["min_accuracy"]
    assert metrics["f1"] >= params["quality_gate"]["min_f1"]


def test_model_can_predict():
    model, _ = train()
    prediction = model.predict(["Ce produit est excellent"])

    assert prediction[0] in [0, 1]
def test_no_regression_vs_baseline():
    params = load_params()
    gate = params["quality_gate"]

    _, metrics = train()

    delta = gate["max_regression"]

    assert metrics["accuracy"] >= (
        gate["baseline_accuracy"] - delta
    )

    assert metrics["f1"] >= (
        gate["baseline_f1"] - delta
    )
def test_quality_gate_accepts_candidate():
    params = load_params()
    gate = params["quality_gate"]

    _, metrics = train()

    accepted = (
        metrics["accuracy"] >= gate["min_accuracy"]
        and metrics["f1"] >= gate["min_f1"]
        and metrics["accuracy"] >= (
            gate["baseline_accuracy"] - gate["max_regression"]
        )
        and metrics["f1"] >= (
            gate["baseline_f1"] - gate["max_regression"]
        )
    )

    assert accepted, "REJECTED: Quality Gate conditions not satisfied"