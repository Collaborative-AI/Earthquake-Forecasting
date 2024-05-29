export CUDA_VISIBLE_DEVICES=0

model_name=TimeMixer
python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/EarthquakeForecasting/ \
  --data_path Various-Catalogs-1.csv \
  --model_id quake-96-12 \
  --model $model_name \
  --data custom \
  --features M \
  --seq_len 48 \
  --label_len 24 \
  --pred_len 12 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 4 \
  --dec_in 4 \
  --c_out 4 \
  --d_model 64 \
  --d_ff 64 \
  --top_k 5 \
  --train_epochs 100 \
  --des Exp \
  --itr 1