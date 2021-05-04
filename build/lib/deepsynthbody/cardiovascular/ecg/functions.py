import deepfakeecg


def generate(num_ecg, out_dir, start_id=0, device="cpu", **kwargs):
    """ Generate DeepFake 12-leads 10-sec long ECG.

    Parameters
    ----------------
    num_ecg: int
        Number of DeepFake ECGs to generate randomly.
    out_dir: str
        A directory to save output files with extension ".asc". 
    start_id: int 
        A interger number to start file names. Default value is 0.and
    device: str
        A device to run the generator. Use strin "cpu" to run on CPU and "cuda" to run on a GPU. 
    
    Return
    ------
    None
        No return value.


    """

    deepfakeecg.generate(num_ecg, out_dir, start_id=start_id, run_device=device, **kwargs)