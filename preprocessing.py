import pandas as pd
import numpy as np
N_FRAME = 30

def feature_extraction(path_list, event_list):
    
    n_dataset = len(path_list)
    path_list_pos = path_list + '_pos.csv'
    path_list_rot = path_list + '_rot.csv'
    
    features_array = np.zeros((n_dataset, (2 * N_FRAME) * 60))
    
    for path_pos, path_rot, event, i in zip(path_list_pos, path_list_rot, event_list, range(n_dataset)):
        pos = pd.read_csv(path_pos, usecols=["Hips.x","Hips.y","Hips.z","RightUpLeg.x","RightUpLeg.y","RightUpLeg.z","RightLeg.x","RightLeg.y","RightLeg.z","RightFoot.x","RightFoot.y","RightFoot.z","LeftUpLeg.x","LeftUpLeg.y","LeftUpLeg.z","LeftLeg.x","LeftLeg.y","LeftLeg.z","LeftFoot.x","LeftFoot.y","LeftFoot.z","Spine.x","Spine.y","Spine.z","Spine1.x","Spine1.y","Spine1.z","Spine2.x","Spine2.y","Spine2.z"])
        rot = pd.read_csv(path_rot, usecols=["Hips.x","Hips.y","Hips.z","RightUpLeg.x","RightUpLeg.y","RightUpLeg.z","RightLeg.x","RightLeg.y","RightLeg.z","RightFoot.x","RightFoot.y","RightFoot.z","LeftUpLeg.x","LeftUpLeg.y","LeftUpLeg.z","LeftLeg.x","LeftLeg.y","LeftLeg.z","LeftFoot.x","LeftFoot.y","LeftFoot.z","Spine.x","Spine.y","Spine.z","Spine1.x","Spine1.y","Spine1.z","Spine2.x","Spine2.y","Spine2.z"])
        pos = pos.iloc[event - N_FRAME: event + N_FRAME, ]
        rot = rot.iloc[event - N_FRAME: event + N_FRAME, ]
        pos_array = pos.to_numpy()
        rot_array = rot.to_numpy()
        feature_array = np.concatenate([pos_array, rot_array], 1)
        features_array[i] = feature_array.reshape((2 * N_FRAME) * 60, )

    return features_array

def main():
    # load training data
    training = pd.read_csv("training.csv")
    path_list = training["path"].to_numpy()
    event_list = training["event"].to_numpy()
    label_list = training["label"].to_numpy()
    
    # extract features of training data
    X_train = feature_extraction(path_list, event_list)
    y_train = np.array(label_list)

    # save preprosessed training data
    np.save('X_train', X_train)
    np.save('y_train', y_train)


if __name__ == "__main__":
    main()
