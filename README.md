func TestBlueprintValidator_Validate(t *testing.T) {
    tests := []struct {
        name     string
        blueprint *Blueprint
        wantErr  bool
    }{
        {
            name: "valid blueprint",
            blueprint: &Blueprint{
                Resources: []Resource{
                    {Kind: "Deployment", Metadata: Metadata{Name: "test"}},
                },
                Metadata: BlueprintMetadata{
                    Timestamp: time.Now(),
                    ClusterInfo: ClusterInfo{
                        Version: "v1.21.0",
                        NodeCount: 3,
                    },
                },
            },
            wantErr: false,
        },
        {
            name: "missing resources",
            blueprint: &Blueprint{
                Resources: nil,
                Metadata: BlueprintMetadata{
                    Timestamp: time.Now(),
                },
            },
            wantErr: true,
        },
        {
            name: "missing timestamp",
            blueprint: &Blueprint{
                Resources: []Resource{
                    {Kind: "Deployment", Metadata: Metadata{Name: "test"}},
                },
                Metadata: BlueprintMetadata{},
            },
            wantErr: true,
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            v := &BlueprintValidator{}
            if err := v.Validate(tt.blueprint); (err != nil) != tt.wantErr {
                t.Errorf("BlueprintValidator.Validate() error = %v, wantErr %v", err, tt.wantErr)
            }
        })
    }
}