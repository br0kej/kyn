from dataclasses import dataclass, asdict
from typing import Dict, Any
import uuid


@dataclass
class KYNConfig:
    learning_rate: float = 5e-4
    min_learning_rate: float = 1e-6
    model_arch: str = "GraphConvInstanceGlobalMaxSmallVariancePreservingEdge"
    data_type: str = "onehopwithcallers"
    train_data: str = "datasets/dummy/binkit-test-new-class-small-graphs.pickle"
    train_labels: str = "datasets/dummy/binkit-test-new-class-small-labels.pickle"
    test_data: str = "datasets/dummy/binkit-test-new-class-small-graphs.pickle"
    test_labels: str = "datasets/dummy/binkit-test-new-class-small-labels.pickle"
    epochs: int = 350
    loss: str = "Circle"
    miner: str = "BatchHard"
    optim: str = "Adam"
    batch_size: int = 256
    model_channels: int = 256
    pooling: str = "max"
    circle_loss_m: float = 0.4
    circle_loss_gamma: int = 80
    num_examples_in_batch: int = 4
    exp_uuid: str = str(uuid.uuid4())[:8]
    feature_dim: int = 6
    dropout_ratio: float = 0.5
    number_eval_sp: int = 500
    with_edges: bool = True
    sampler_epoch_size: int = 100000

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass instance to a dictionary.
        Filters out None values by default."""
        return {k: v for k, v in asdict(self).items() if v is not None}
