import torch
import torch.nn as nn


class iAFF(nn.Module):
    '''
    多特征融合 iAFF
    '''

    def __init__(self, num_channels=80, r=4):
        super(iAFF, self).__init__()
        inter_channels = int(num_channels // r)

        # 本地注意力
        self.local_att = nn.Sequential(
            nn.Conv1d(num_channels, inter_channels, kernel_size=3, padding=1),
            nn.BatchNorm1d(inter_channels),
            nn.ReLU(inplace=True),
            nn.Conv1d(inter_channels, num_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(num_channels),
        )

        # 全局注意力
        self.global_att = nn.Sequential(
            nn.AdaptiveAvgPool1d(1),
            nn.Conv1d(num_channels,inter_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(inter_channels),
            nn.ReLU(inplace=True),
            nn.Conv1d(inter_channels,num_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(num_channels),
        )

        # 第二次本地注意力
        self.local_att2 = nn.Sequential(
            nn.Conv1d(num_channels,inter_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(inter_channels),
            nn.ReLU(inplace=True),
            nn.Conv1d(inter_channels,num_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(num_channels),
        )
        # 第二次全局注意力
        self.global_att2 = nn.Sequential(
            nn.AdaptiveAvgPool1d(1),
            nn.Conv1d(num_channels,inter_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(inter_channels),
            nn.ReLU(inplace=True),
            nn.Conv1d(inter_channels,num_channels,kernel_size=3,padding=1),
            nn.BatchNorm1d(num_channels),
        )

        self.sigmoid = nn.Sigmoid()

    def forward(self, x, residual): #N,L,H
        x = x.permute(0, 2, 1)
        residual = residual.permute(0, 2, 1)
        xa = x + residual
        xl = self.local_att(xa)
        xg = self.global_att(xa)
        xlg = xl + xg
        wei = self.sigmoid(xlg)
        xi = x * wei + residual * (1 - wei) #N,L,H

        xl2 = self.local_att2(xi)
        xg2 = self.global_att2(xi)
        xlg2 = xl2 + xg2
        wei2 = self.sigmoid(xlg2)
        xo = x * wei2 + residual * (1 - wei2)
        xo = xo.permute(0, 2, 1)
        return xo

"""
input = torch.randn(50, 64, 35)
input2 = torch.randn(50, 64, 35)
iaff = iAFF()
out = iaff.forward(input,input2)
print(out.size())
"""
